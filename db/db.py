import pandas as pd
import re
import psycopg2
from psycopg2 import Error, extras


def getConnection():
    try:
        connection = psycopg2.connect(
            user='admin',
            password='admin',
            host='127.0.0.1',
            port='5432',
            database='aera'
        )
        # Create a cursor to perform database operations
        return connection
    except Exception as error:
        print('Error while connecting to PostgreSQL', error)

def findCourseByName(course_name):
    conn = getConnection()
    cursor = conn.cursor(cursor_factory= extras.RealDictCursor)
    cursor.execute('SELECT nombre, codigo FROM cursos WHERE lower(nombre) ~ ')


def getCoursesAndCodes():
    conn = getConnection()

    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)

    cursor.execute('SELECT nombre, codigo FROM cursos ORDER BY nombre ASC;')

    cursos = cursor.fetchall()

    cursor.close()
    conn.close()
    return cursos


def getCourses():
    df = pd.read_csv('db/courses.csv')
    allCourses = df['courses'].values.tolist()
    return allCourses


def getCourseSchedule(course_code, section):
    conn = getConnection()
    cursor = conn.cursor(cursor_factory= extras.RealDictCursor)
    print(course_code, ' ', section)

    query = '''
                    Select 
                        dia, 
                        tipo_clase, 
                        to_char(empieza_en, 'HH12:MI AM') as empieza_en, 
                        to_char(termina_en , 'HH12:MI AM') as termina_en 
                    from cursos_horarios 
                    WHERE lower(cod_curso) = %s and lower(seccion) = %s 
                    ORDER BY dia ASC;
                    '''
    cursor.execute(query, (course_code.lower(), section.lower()))
    
    schedule = cursor.fetchall()
    return schedule
    

def getCourseRoom(course_code, section):
    conn = getConnection()
    cursor = conn.cursor(cursor_factory= extras.RealDictCursor)
    print(course_code, ' ', section)

    query = '''
                    Select 
                        dia, 
                        tipo_clase,
                        aula, 
                        to_char(empieza_en, 'HH12:MI AM') as empieza_en, 
                        to_char(termina_en , 'HH12:MI AM') as termina_en 
                    from cursos_horarios 
                    WHERE lower(cod_curso) = %s and lower(seccion) = %s 
                    ORDER BY dia ASC;
                    '''
    cursor.execute(query, (course_code.lower(), section.lower()))
    
    curso_rooms = cursor.fetchall()
    return curso_rooms

def getCourseSchedule2(course, section):
    return [{
            'day': 'Lunes',
            'start': '8pm',
            'end': '10am',
            'type': 'Teoria'},
            {
            'day': 'Martes',
            'start': '2pm',
            'end': '4pm',
            'type': 'Practica'}]


def getSectionsCourseByCode(code):
    conn = getConnection()
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)

    cursor.execute('''with secctions as ( select DISTINCT lower(seccion) as seccion  FROM cursos_horarios WHERE cod_curso = %s) 
                select * from secctions order by seccion;''',
                   (code,))

    sections = cursor.fetchall()
    sections = [sec['seccion'] for sec in sections]
    
    return sections


def getSectionsCourse(course):
    df = pd.read_excel('db/Insumos Matrícula SIGA 2022-1 (1).xlsx',
                       sheet_name='HorariosConfiguracionCursoSecci')
    df['NOMBRE DEL CURSO'] = df['NOMBRE DEL CURSO'].apply(lambda x: x.lower())
    sections = df[df['NOMBRE DEL CURSO'] ==
                  course.lower()]['SECCION'].values.tolist()
    sections = list(set(sections))
    sections.sort()
    return sections


aulas = ['J3-102','J3 122','J3-202', 'R1 460']

j3_aulas = [ aula for aula in aulas if re.search('^J', aula, re.IGNORECASE) ]
first_floor_j3 = [j3_aula for j3_aula in j3_aulas if re.search('^(J3(\s|\-)?1)', j3_aula, re.IGNORECASE)]
        
print(j3_aulas)

print(first_floor_j3)

r_aulas = [ aula for aula in aulas if re.search('^R\d?', aula, re.IGNORECASE) ]

floors_r = [
                        [
                        r_aula for r_aula in r_aulas 
                            if re.search(f'^(R\d(\s|\-)?{i})', r_aula, re.IGNORECASE)
                        ] for i in range(1,5)
                    ] 
print(floors_r)
#sections = getSectionsCourseByCode('BEF01')
#print(sections)
#slot_value = 'algoritmos'

#courses = getCourses()

# if slot_value in courses:
#    print(slot_value)

#matches = [ course for course in courses if re.search(slot_value, course)]
