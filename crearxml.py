#Importamos xml.etree con el nombre ET que nos ayudara a hacer el xml
import xml.etree.ElementTree as ET

#Creamos funcion para crear xml
def crear_xml():
    #Elemento root
    p = ET.Element('students')
    
    #Elementos childs
    c1 = ET.SubElement(p, 'student')
    c2 = ET.SubElement(p, 'student')
    c3 = ET.SubElement(p, 'student')
    c4 = ET.SubElement(p, 'student')
    c5 = ET.SubElement(p, 'student')
    
    #Elementos sub-child1
    s1_c1 = ET.SubElement(c1, 'name')
    s2_c1 = ET.SubElement(c1, 'surname')
    s3_c1 = ET.SubElement(c1, 'email')
    s4_c1 = ET.SubElement(c1, 'dni')
    #Añadir datos
    s1_c1.text = 'Raul'
    s2_c1.text = 'Vaquerizo'
    s3_c1.text = 'raulvt2003@gmail.com'
    s4_c1.text = '4829825b'
    
    #Elementos sub-child2
    s1_c2 = ET.SubElement(c2, 'name')
    s2_c2 = ET.SubElement(c2, 'surname')
    s3_c2 = ET.SubElement(c2, 'email')
    s4_c2 = ET.SubElement(c2, 'dni')
    #Añadir datos
    s1_c2.text = 'Herson'
    s2_c2.text = 'Vega'
    s3_c2.text = 'hvega@gmail.com'
    s4_c2.text = '48256822b'
    
    
    #Elementos sub-child3
    s1_c3 = ET.SubElement(c3, 'name')
    s2_c3 = ET.SubElement(c3, 'surname')
    s3_c3 = ET.SubElement(c3, 'email')
    s4_c3 = ET.SubElement(c3, 'dni')
    #Añadir datos
    s1_c3.text = 'Leo'
    s2_c3.text = 'Chavez'
    s3_c3.text = 'lchavez@gmail.com'
    s4_c3.text = '48445822b'
    
    #Elementos sub-child4
    s1_c4 = ET.SubElement(c4, 'name')
    s2_c4 = ET.SubElement(c4, 'surname')
    s3_c4 = ET.SubElement(c4, 'email')
    s4_c4 = ET.SubElement(c4, 'dni')
    #Añadir datos
    s1_c4.text = 'Aitor'
    s2_c4.text = 'Monge'
    s3_c4.text = 'amonge@gmail.com'
    s4_c4.text = '48445822b'
    
    #Elementos sub-child5
    s1_c5 = ET.SubElement(c5, 'name')
    s2_c5 = ET.SubElement(c5, 'surname')
    s3_c5 = ET.SubElement(c5, 'email')
    s4_c5 = ET.SubElement(c5, 'dni')
    #Añadir datos
    s1_c5.text = 'Matias'
    s2_c5.text = 'Rodriguez'
    s3_c5.text = 'mrodri@gmail.com'
    s4_c5.text = '48443212b'
    
    
    #añadir atributos a cada child
    c1.set('clase','DAW')
    c2.set('clase','DAW')
    c3.set('clase','DAW')
    c4.set('clase','DAW')
    c5.set('clase','DAW')
    
    #Indentar (dar formato)
    ET.indent(p)
    
    #Guardar aquest xml amb la funció ElementTree()
    tree = ET.ElementTree(p)
    tree.write('students.xml')

    #Mostrar por consola el xml
    ET.dump(tree)

#Llamada a la funcion
crear_xml()