#!/usr/bin/env python3
"""Generate neural network diagrams using pydot"""

import pydot
import os

# Ensure images directory exists
os.makedirs('images', exist_ok=True)

# ==========================================
# Simple Network Diagram (2-3-1)
# ==========================================
graph1 = pydot.Dot(graph_type='digraph', rankdir='LR', bgcolor='white')
graph1.set_node_defaults(shape='circle', style='filled', fontname='Arial')
graph1.set_edge_defaults(color='gray', arrowsize='0.8')

# Input layer nodes
input_nodes = []
for i in range(2):
    node_name = f'x{i+1}'
    label = f'x₁' if i == 0 else f'x₂'
    node = pydot.Node(node_name, label=label, fillcolor='lightblue', 
                     fontsize='12', width='0.6')
    graph1.add_node(node)
    input_nodes.append(node_name)

# Hidden layer nodes
hidden_nodes = []
for i in range(3):
    node_name = f'h{i+1}'
    label = f'h{i+1}'
    node = pydot.Node(node_name, label=label, fillcolor='lightgreen',
                     fontsize='12', width='0.6')
    graph1.add_node(node)
    hidden_nodes.append(node_name)

# Output layer node
output_node = pydot.Node('y', label='ŷ', fillcolor='lightyellow',
                        fontsize='12', width='0.6')
graph1.add_node(output_node)

# Add edges from input to hidden layer
for input_n in input_nodes:
    for hidden_n in hidden_nodes:
        edge = pydot.Edge(input_n, hidden_n, penwidth='1.5')
        graph1.add_edge(edge)

# Add edges from hidden to output layer
for hidden_n in hidden_nodes:
    edge = pydot.Edge(hidden_n, 'y', penwidth='1.5')
    graph1.add_edge(edge)

# Save the first graph
graph1.write_png('images/neural_network_simple.png')
print("Created: images/neural_network_simple.png")

# ==========================================
# Digit Recognition Network (64-128-10)
# ==========================================
graph2 = pydot.Dot(graph_type='digraph', rankdir='LR', bgcolor='white')
graph2.set_node_defaults(shape='circle', style='filled', fontname='Arial')
graph2.set_edge_defaults(color='lightgray', arrowsize='0.5')

# Input layer (show subset of 64 neurons)
input_sample = [0, 15, 31, 47, 63]  # Sample pixels from 64
input_nodes = []
for i in input_sample:
    node_name = f'pixel_{i}'
    label = f'p{i}'
    node = pydot.Node(node_name, label=label, fillcolor='lightblue',
                     fontsize='10', width='0.4', height='0.4')
    graph2.add_node(node)
    input_nodes.append(node_name)

# Add ellipsis for input layer
graph2.add_node(pydot.Node('input_dots', label='⋮', shape='plaintext',
                         fontsize='20', fontcolor='blue'))

# Hidden layer (show subset of neurons)
hidden_sample = range(5)  # Show 5 of the hidden neurons
hidden_nodes = []
for i in hidden_sample:
    node_name = f'hidden_{i}'
    label = f'h{i}'
    node = pydot.Node(node_name, label=label, fillcolor='lightgreen',
                     fontsize='10', width='0.4', height='0.4')
    graph2.add_node(node)
    hidden_nodes.append(node_name)

# Add ellipsis for hidden layer
graph2.add_node(pydot.Node('hidden_dots', label='⋮', shape='plaintext',
                         fontsize='20', fontcolor='green'))

# Output layer (all 10 digits)
output_nodes = []
for i in range(10):
    node_name = f'digit_{i}'
    label = str(i)
    node = pydot.Node(node_name, label=label, fillcolor='lightyellow',
                     fontsize='10', width='0.4', height='0.4')
    graph2.add_node(node)
    output_nodes.append(node_name)

# Add sample edges (not all connections shown for clarity)
for input_n in input_nodes[:3]:  # Sample connections
    for hidden_n in hidden_nodes[:3]:
        edge = pydot.Edge(input_n, hidden_n, penwidth='0.5', style='dashed')
        graph2.add_edge(edge)

for hidden_n in hidden_nodes[:3]:
    for output_n in output_nodes[::3]:  # Sample connections
        edge = pydot.Edge(hidden_n, output_n, penwidth='0.5', style='dashed')
        graph2.add_edge(edge)

# Save the second graph
graph2.write_png('images/neural_network_digits.png')
print("Created: images/neural_network_digits.png")

print("\nBoth network diagrams have been created successfully!")
print("\nAfter pushing to GitHub, you can reference them in the notebook with:")
print("  - https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/images/neural_network_simple.png")
print("  - https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/images/neural_network_digits.png")