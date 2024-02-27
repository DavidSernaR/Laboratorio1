import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Conjuntos de datos
set1 = {'A', 'B', 'C', 'D'}
set2 = {'B', 'C', 'D', 'E'}
set3 = {'C', 'D', 'E', 'F'}

# Crear el diagrama de Venn
venn_diagram = venn3([set1, set2, set3], ('Set 1', 'Set 2', 'Set 3'))

# Personalizar el diagrama (opcional)
venn_diagram.get_label_by_id('100').set_text('\n'.join(set1 - set2 - set3))  # Elementos solo en el primer conjunto
venn_diagram.get_label_by_id('010').set_text('\n'.join(set2 - set1 - set3))  # Elementos solo en el segundo conjunto
venn_diagram.get_label_by_id('110').set_text('\n'.join(set1 & set2 - set3))  # Elementos en conjuntos 1 y 2
venn_diagram.get_label_by_id('001').set_text('\n'.join(set3 - set1 - set2))  # Elementos solo en el tercer conjunto
venn_diagram.get_label_by_id('101').set_text('\n'.join(set1 & set3 - set2))  # Elementos en conjuntos 1 y 3
venn_diagram.get_label_by_id('011').set_text('\n'.join(set2 & set3 - set1))  # Elementos en conjuntos 2 y 3
venn_diagram.get_label_by_id('111').set_text('\n'.join(set1 & set2 & set3))  # Elementos en los tres conjuntos

# Mostrar el diagrama
plt.title("Diagrama de Venn")
plt.show()
