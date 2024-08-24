import gradio as gr
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder


Parametros = ['Gender', 'Age', 'GPA', 'Interested Domain', 'Projects', 'Python', 'SQL', 'Java']

Interes = ['Artificial Intelligence', 'Data Science', 'Software Development',
 'Web Development', 'Cybersecurity', 'Machine Learning',
 'Database Management', 'Cloud Computing', 'Mobile App Development',
 'Computer Graphics', 'Software Engineering', 'Network Security',
 'Game Development', 'Computer Vision', 'Bioinformatics',
 'IoT (Internet of Things)', 'Natural Language Processing', 'Data Mining',
 'Human-Computer Interaction', 'Biomedical Computing', 'Quantum Computing',
 'Blockchain Technology', 'Information Retrieval', 'Data Privacy',
  'Geographic Information Systems', 'Distributed Systems',
 'Digital Forensics']

Proyectos = ['Chatbot Development', 'Data Analytics', 'E-commerce Website',
 'Full-Stack Web App', 'Network Security', 'Image Recognition',
 'SQL Query Optimization', 'AWS Deployment', 'Android App', '3D Rendering',
 'Natural Language Processing', 'iOS App', 'Game Development',
 'GCP Deployment', 'Social Media Platform', 'iOS Game' '3D Animation',
 'Machine Learning', 'Android Game', '3D Modeling', 'Firewall Management',
 'Deep Learning Models', 'Data Warehouse Design', 'Embedded Systems',
 'Front-End Development', 'Statistical Analysis', 'Robotics',
 'Mobile Game Development', 'Penetration Testing', 'Object Detection',
 'DevOps', 'Genomic Data Analysis', 'Smart Home Automation',
 'Market Analysis', 'Cloud Migration Specialist', 'Usability Testing',
 'Medical Imaging Analysis', 'Quantum Algorithm Development',
 'Virtual Reality Development', 'Smart Contracts Developer',
 'Search Engine Optimization', 'Privacy Compliance Officer', 'GIS Mapping',
 'Distributed Systems Architect', 'Computer Forensic Analyst',
 'Protein Structure Prediction', 'User Experience Researcher',
  'Healthcare Data Analyst', 'Neural Network Development',
 'Big Data Analytics', 'Mobile App Development', 'Image Classification',
 'SQL Database Design', 'Cloud Infrastructure Management',
 'iOS App Development', 'Android App Development',
 'Enterprise Software Development', 'Computer Vision',
 'Web Application Development', 'Security Auditing',
 'SQL Database Administration', 'Cloud Solution Architecture',
 'Cross-Platform App Development', 'Reinforcement Learning', 'Data Mining']

Lenguajes = ['Weak', 'Average', 'Strong']

Future_careers = ['Machine Learning Researcher', 'Data Scientist', 'Software Engineer',
 'Web Developer', 'Information Security Analyst',
 'Machine Learning Engineer', 'Database Administrator',
 'Cloud Solutions Architect', 'Mobile App Developer', 'Graphics Programmer',
 'NLP Research Scientist', 'Game Developer', 'Security Analyst',
 'Embedded Software Engineer', 'Data Analyst', 'Robotics Engineer',
 'Ethical Hacker', 'Computer Vision Engineer', 'DevOps Engineer',
 'Bioinformatician', 'IoT Developer', 'NLP Engineer', 'UX Designer',
 'Healthcare IT Specialist', 'Quantum Computing Researcher', 'VR Developer',
 'Blockchain Engineer', 'SEO Specialist', 'Data Privacy Specialist',
 'Geospatial Analyst', 'Distributed Systems Engineer',
 'Digital Forensics Specialist', 'AI Researcher']

Gender = ['Male', 'Female']

nombre = 'Modelo/Best_model.pkl'
best_model = pickle.load(open(nombre, 'rb'))

LE = LabelEncoder()
LE.fit(Future_careers)
LE0 = LabelEncoder()
LE0.fit(Gender)
LE1 = LabelEncoder()
LE1.fit(Proyectos)
LE2 = LabelEncoder()
LE2.fit(Interes)

def predecir(*args):
    Datos = {}

    for i in range(len(Parametros)):
        Datos[Parametros[i]] = [args[i]]

    df = pd.DataFrame.from_dict(Datos)
    categorical_columns = ['Gender', 'Interested Domain','Projects']
    df['Gender'] = LE0.transform(df['Gender'])
    df['Interested Domain'] = LE2.transform(df['Interested Domain'])
    df['Projects'] = LE1.transform(df['Projects'])
    OE = OrdinalEncoder(categories=[['Weak', 'Average', 'Strong']])
    Ordinal_columns = ['Python', 'SQL', 'Java']
    for i in Ordinal_columns:
        df[i] = OE.fit_transform(df[[i]])

    prediccion = best_model.predict(df)

    return f"Carrera: {LE.inverse_transform(prediccion)[0]}"

with gr.Blocks() as demo:
  gr.Markdown(
    """ 
    # 📚 Computer Science Students Career Prediction
    """
  )
  with gr.Row():
    with gr.Column():
      gr.Markdown(
        """ 
        ## 📃 Personal Information
        """
      )     
      with gr.Row():
        Gender = gr.Radio(['Male', 'Female'] ,label="Gender")
        Age = gr.Number(label="Age", precision = 0, minimum = 0, maximum = 100)
        GPA = gr.Number(label="GPA", precision = 2, minimum = 0.0, maximum = 5.0)
      gr.Markdown(
        """ 
        ## 📈 Lenguage Level
        """
      )
      with gr.Row():
        Java = gr.Dropdown(Lenguajes, label="Java")
        Python = gr.Dropdown(Lenguajes, label="Python")
        SQL = gr.Dropdown(Lenguajes, label="SQL")
      gr.Markdown(
        """ 
        ## 🏫 Academic Information
        """
      )
      with gr.Row():
        Projects = gr.Dropdown(Proyectos, label="Projects")
        Interested_Domain = gr.Dropdown(Interes, label="Interested Domain")

    with gr.Column():
      gr.Markdown(
        """
        ## 🎯 Prediction
        """
      )
      label = gr.Label()
      boton = gr.Button(value = 'Submit')
      boton.click(predecir,
                 inputs = [Gender, 
                           Age, 
                           GPA, 
                           Interested_Domain, 
                           Projects,
                           Python, 
                           SQL, 
                           Java],
                 outputs = [label],
                 )
demo.launch()