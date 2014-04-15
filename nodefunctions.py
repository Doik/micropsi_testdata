

def humbug(nodenet, node=None, **params):

    import pdb; pdb.set_trace()
    gen = node.get_slot('gen').activation
    hum = node.get_slot('hum').activation
    bug = node.get_slot('bug').activation

    node.activation = gen + hum + bug

    node.get_gate("gen").gate_function(node.activation)
    node.get_gate("hum").gate_function(node.activation)
    node.get_gate("bug").gate_function(node.activation)
