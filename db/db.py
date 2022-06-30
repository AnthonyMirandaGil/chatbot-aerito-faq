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

def getSectionsCourseByCode(code):
    conn = getConnection()
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)

    cursor.execute('''with secctions as ( select DISTINCT lower(seccion) as seccion  FROM cursos_horarios WHERE cod_curso = %s) 
                select * from secctions order by seccion;''',
                   (code,))

    sections = cursor.fetchall()
    sections = [sec['seccion'] for sec in sections]
    
    return sections


#sections = getSectionsCourseByCode('BEF01')
#print(sections)
#slot_value = 'algoritmos'

#courses = getCourses()

# if slot_value in courses:
#    print(slot_value)

#matches = [ course for course in courses if re.search(slot_value, course)]
