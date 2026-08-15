
bl_info = {
    "name": "Date Palm Bunch Generator - مولد عذق التمر",
    "author": "Saeed (hashtag4ae) with Claude",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "location": "Add > Curve > Date Bunch  |  اضافة > منحنى > عذق تمر",
    "description": "One-click realistic date palm bunches. 23 Saudi date varieties, collision-free fruits, full sliders.",
    "category": "Add Curve",
}

import bpy, math, random, os
from bpy.props import IntProperty, FloatProperty

ASSET_BLEND = os.path.join(os.path.dirname(__file__), "date_bunch_assets.blend")

NEEDED_OBJECTS = ("DateFruit", "WrinkleSpace")


def ensure_assets():
    ng = bpy.data.node_groups.get("GN_DateBunch")
    have_objs = all(bpy.data.objects.get(o) for o in NEEDED_OBJECTS)
    if not (ng and have_objs):
        with bpy.data.libraries.load(ASSET_BLEND, link=False) as (df, dt):
            if not ng:
                dt.node_groups = [n for n in df.node_groups if n == "GN_DateBunch"]
            dt.objects = [o for o in df.objects
                          if o in NEEDED_OBJECTS and not bpy.data.objects.get(o)]
    coll = bpy.data.collections.get("DateBunch_Support")
    if not coll:
        coll = bpy.data.collections.new("DateBunch_Support")
        bpy.context.scene.collection.children.link(coll)
    for name in NEEDED_OBJECTS:
        o = bpy.data.objects.get(name)
        if o and o.name not in coll.objects:
            try:
                coll.objects.link(o)
            except RuntimeError:
                pass
        if o:
            o.hide_set(True)
    return (bpy.data.node_groups.get("GN_DateBunch"),
            bpy.data.objects.get("DateFruit"))


def build_curves(cu, n_strands, seed, spread, length_mul):
    cu.splines.clear()

    def add_spline(pts, radii):
        sp = cu.splines.new('BEZIER')
        sp.bezier_points.add(len(pts) - 1)
        for bp, co, r in zip(sp.bezier_points, pts, radii):
            bp.co = co
            bp.handle_left_type = 'AUTO'
            bp.handle_right_type = 'AUTO'
            bp.radius = r

    rnd = random.Random(seed)
    add_spline([(0, 0, 0.20), (0.004, -0.002, 0.10), (0.0, 0.002, 0.02), (0, 0, -0.07)],
               [1.8, 1.6, 1.4, 1.1])
    for i in range(n_strands):
        a = i * (2 * math.pi / n_strands) + rnd.uniform(-0.22, 0.22)
        z0 = 0.035 - 0.10 * (i / max(1, n_strands - 1)) + rnd.uniform(-0.006, 0.006)
        r1 = rnd.uniform(0.03, 0.048) * spread
        r2 = rnd.uniform(0.07, 0.10) * spread
        r3 = r2 * rnd.uniform(0.75, 0.95)
        zend = z0 - rnd.uniform(0.22, 0.34) * length_mul
        pts = [
            (0.0, 0.0, z0),
            (r1 * math.cos(a), r1 * math.sin(a), z0 - 0.06 + rnd.uniform(-0.01, 0.01)),
            (r2 * math.cos(a + 0.12), r2 * math.sin(a + 0.12), z0 - 0.16 * length_mul + rnd.uniform(-0.015, 0.015)),
            (r3 * math.cos(a + 0.24), r3 * math.sin(a + 0.24), zend),
        ]
        add_spline(pts, [1.0, 0.85, 0.7, 0.5])


def setup_wrinkle_drivers(bunch, fruit, ng):
    idents = {s.name: s.identifier for s in ng.interface.items_tree
              if getattr(s, "in_out", None) == 'INPUT'}
    mapping = [("Wrinkles", "strength", "Fruit Wrinkles", False),
               ("Lumps", "strength", "Fruit Lumps", False),
               ("Micro", "strength", "Fruit Micro", False),
               ("Subd", "levels", "Fruit Resolution", True),
               ("Subd", "render_levels", "Fruit Resolution", True)]
    for mod_name, path, sock, is_int in mapping:
        m = fruit.modifiers.get(mod_name)
        if not m or sock not in idents:
            continue
        try:
            m.driver_remove(path)
        except Exception:
            pass
        fc = m.driver_add(path)
        d = fc.driver
        d.type = 'SCRIPTED'
        v = d.variables.new()
        v.name = "v"
        v.type = 'SINGLE_PROP'
        v.targets[0].id_type = 'OBJECT'
        v.targets[0].id = bunch
        v.targets[0].data_path = 'modifiers["DateBunchGN"]["%s"]' % idents[sock]
        d.expression = "int(v)" if is_int else "v"


class CURVE_OT_add_date_bunch(bpy.types.Operator):
    """Add a realistic procedural date palm bunch / اضف عذق تمر واقعي"""
    bl_idname = "curve.add_date_bunch"
    bl_label = "Date Bunch (عذق تمر)"
    bl_options = {'REGISTER', 'UNDO'}

    strands: IntProperty(name="Strands / عدد الشماريخ", default=11, min=3, max=24)
    seed: IntProperty(name="Shape Seed / شكل عشوائي", default=9, min=0, max=1000)
    spread: FloatProperty(name="Spread / اتساع", default=1.0, min=0.4, max=2.5)
    length: FloatProperty(name="Length / طول الشماريخ", default=1.0, min=0.4, max=2.0)
    scale: FloatProperty(name="Overall Size / الحجم الكلي", default=2.7, min=0.1, max=20.0)
    variety: IntProperty(name="Variety / الصنف (0-22)", default=0, min=0, max=22)

    def execute(self, context):
        ng, fruit = ensure_assets()
        if not ng or not fruit:
            self.report({'ERROR'}, "date_bunch_assets.blend not found next to the addon")
            return {'CANCELLED'}
        cu = bpy.data.curves.new("DateBunchCurves", 'CURVE')
        cu.dimensions = '3D'
        build_curves(cu, self.strands, self.seed, self.spread, self.length)
        ob = bpy.data.objects.new("DateBunch", cu)
        context.collection.objects.link(ob)
        ob.location = context.scene.cursor.location
        ob.scale = (self.scale, self.scale, self.scale)
        mod = ob.modifiers.new("DateBunchGN", 'NODES')
        mod.node_group = ng
        defaults = {"Strands x": 1, "Date Spacing": 0.05, "Date Size": 1.0,
                    "Dates Start": 0.25, "Stalk Radius": 0.0028, "Knob Size": 0.0032,
                    "Fruit Wrinkles": 0.32, "Fruit Lumps": 0.13, "Fruit Micro": 0.08,
                    "Fruit Resolution": 1, "Stalk Resolution": 8,
                    "Color Seed": self.seed, "Variety": self.variety}
        for s in ng.interface.items_tree:
            if getattr(s, "in_out", None) == 'INPUT' and s.name in defaults:
                v = defaults[s.name]
                mod[s.identifier] = int(v) if s.socket_type == 'NodeSocketInt' else float(v)
        setup_wrinkle_drivers(ob, fruit, ng)
        for o in context.selected_objects:
            o.select_set(False)
        ob.select_set(True)
        context.view_layer.objects.active = ob
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(CURVE_OT_add_date_bunch.bl_idname, icon='OUTLINER_OB_CURVES')


def register():
    bpy.utils.register_class(CURVE_OT_add_date_bunch)
    bpy.types.VIEW3D_MT_curve_add.append(menu_func)


def unregister():
    bpy.types.VIEW3D_MT_curve_add.remove(menu_func)
    bpy.utils.unregister_class(CURVE_OT_add_date_bunch)


if __name__ == "__main__":
    register()
