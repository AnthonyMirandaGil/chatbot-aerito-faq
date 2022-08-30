import nltk
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")


answers = [
    {
        "answer": "razones de salud, trabajo o de otra naturaleza debidamente sustentada",
        "context": "la, realizada por solicitud, procede por razones de salud, trabajo o de otra naturaleza debidamente sustentada, para tal efecto el estudiante adjuntar",
        "document": {
            "content": "CAPÍTULO VII Procedimiento de Reserva de Matrícula Art. 73º UJ ,J z º G' z m El estudiante o apoderado deberá presentar la solicitud de Reserva de Matrícula al Decano, a través de la plataforma SIGA-ORCE, a más tardar cinco (5) días hábiles antes de la semana oficial de matrícula. La reserva de matrícula, realizada por solicitud, procede por razones de salud, trabajo o de otra naturaleza debidamente sustentada, para tal efecto el estudiante adjuntará los documentos que acrediten la razón invocada En caso no se presente esta solicitud y el estudiante no haya concretado su matrícula, la ORCE realizará, de oficio, la reserva de matrícula del estudiante. El jefe de la Oficina de Estadística de la Facultad que monitorea el proceso, pondrá a disposición del Comité Directivo de la Escuela Profesional las solicitudes de reserva de matrícula presentadas por los estudiantes, aprobará los que cumplan los requisitos previstos y elevará informe al Consejo de Facultad, con las sustentaciones presentadas. La Escuela profesional remitirá a la ORCE el listado de reservas de matrícula aprobadas, para su registro en el SIGA-ORCE, por lo menos dos días hábiles antes del primer día de matrícula de la Facultad. La ORCE registrará la reserva de matrícula en el historial del estudiante (desactivación del código de estudiante).",
            "content_type": "text",
            "id": "a1b3a1a29b2cce2ec9115e3249b6e877",
            "meta": {},
            "score": 0.5312093733737563
        },
        "document_id": "a1b3a1a29b2cce2ec9115e3249b6e877",
        "meta": {},
        "offsets_in_context": [
            {
                "end": 110,
                "start": 41
            }
        ],
        "offsets_in_document": [
            {
                "end": 413,
                "start": 344
            }
        ],
        "score": 0.5835930109024048,
        "type": "extractive"
    },
    {
        "answer": "salud, trabajo o de otras naturaleza debidamente sustentada",
        "context": "ealizada por solicitud procede por razones de salud, trabajo o de otras naturaleza debidamente sustentada, para tal efecto el estudiante adjuntará los",
        "document": {
            "content": "RESERVA DE MATRÍCULA Procedimiento de Reserva de Matrícula El estudiante o apoderado deberá presentar la solicitud de Reserva de Matrícula al Decano, a través de la plataforma SIGA-ORCE, a más tardar cinco (5) días hábiles antes de la semana oficial de matrícula. La reserva de matrícula, realizada por solicitud procede por razones de salud, trabajo o de otras naturaleza debidamente sustentada, para tal efecto el estudiante adjuntará los documentos que acrediten la razón invocada. En caso no se presente esta solicitud y el estudiante no haya concretado su matrícula, la ORCE realizará, de oficio, la reserva de matrícula del estudiante. El jefe de la Oficina de Estadística de la Facultad que monitorea el proceso, pondrá a disposición del Comité Directivo de la Escuela Profesional las solicitudes de reserva de matrícula presentadas por los estudiantes, aprobará las que cumplan los requisitos previstos y elevará informe al Consejo de Facultad, con las sustentaciones presentadas. La Escuela profesional remitirá a la ORCE el listado de reservas de matrícula aprobadas, para su registro en el SIGA-ORCE, por lo menos dos días hábiles antes del primer día de matrícula de la Facultad. La ORCE registrará la reserva de matrícula en el historial del estudiante (desactivación del código de estudiante). (ver modelo de solicitud en la siguiente hoja) SOLICITO: RESERVA DE MATRÍCULA SEÑOR DECANO DE LA FACULTAD DE CIENCIAS DE LA UNIVERSIDAD NACIONAL DE INGENIERÍA Yo,…………………………………………………………………………………… alumno de la Facultad de Ciencias, con código de alumno …………………..., perteneciente a la especialidad de ………………………………………..........., ante usted expongo: Que, por motivos de ….............................................., no podré matricularme y continuar mis estudios en el periodo académico ….........…......., por ello solicito que autorice la reserva de mi matrícula por …............ vez. POR LO EXPUESTO: Ruego a usted, atender a la brevedad mi petición por ser justa.",
            "content_type": "text",
            "id": "dc788523ed8b51c0b3a78b5b2a3ec01e",
            "meta": {},
            "score": 0.5312093733737563
        },
        "document_id": "dc788523ed8b51c0b3a78b5b2a3ec01e",
        "meta": {},
        "offsets_in_context": [
            {
                "end": 105,
                "start": 46
            }
        ],
        "offsets_in_document": [
            {
                "end": 395,
                "start": 336
            }
        ],
        "score": 0.571504533290863,
        "type": "extractive"
    },
    {
        "answer": "motivos de fuerza mayor",
        "context": "11 CONCEPTOS Y NORMAS DEL PROCESO DE MATRÍCULA Procede sólo por motivos de fuerza mayor y se podrá presentar hasta el último día útil de la penúltima ",
        "document": {
            "content": "CAPÍTULO 11 CONCEPTOS Y NORMAS DEL PROCESO DE MATRÍCULA Procede sólo por motivos de fuerza mayor y se podrá presentar hasta el último día útil de la penúltima semana de clases. No procede un retiro Total cuando el estudiante ha rendido todas las evaluaciones regulares de alguna de las asignaturas en la que se encuentra matriculado o si en los dos ciclos regulares precedentes ha optado por el retiro total o si tiene algún curso desaprobado dos veces o más al periodo académico regular precedente. Los estudiantes que soliciten el retiro total deberán adjuntar la debida documentación que sustente los motivos por los cuales solita dicha medida. e. Retiro Reglamentario: Es el procedimiento de oficio ejecutado por ORCE que elimina la matrícula del estudiante, por contravenir al presente reglamento. Pudiendo ser: por eliminación de la asignatura-sección, por registro convalidatorio tardío que hace innecesaria una matrícula obligatoria, por no haber aprobado prerrequisito, o por activación irregular del código de alumno separado temporalmente o retirado definitivamente, etc.\nf.\nRetiro Definitivo: es el procedimiento voluntario o de oficio mediante el cual un estudiante es desvinculado de manera definitiva de la UNI. Procede a solicitud del estudiante ante su Decano o por mandato de Resolución Decana! o Rectoral, · motivada por falta disciplinaria muy grave, por Exceso de Licencia o por Bajo Rendimiento Académico, conforme a ley y los reglamentos de la UNI. g.\nReserva de Matrícula: es la situación a la que pasa aquel estudiante que ha decidido dejar de estudiar por uno o más periodos académicos (suspensión voluntaria). Ejerce así su derecho de postergar su matrícula. ORCE, al cierre de la Matrícula, la registra de oficio para aquellos estudiantes que no se matricularon. La reserva de matrícula suspende la permanencia y evita la pérdida de su condición de estudiante de la UNI. El período de reserva de matrícula no excederá a los tres (03) años (o seis semestres) académicos consecutivos o alternos (equivalente a 06 periodos académicos).",
            "content_type": "text",
            "id": "30bbc99e952a511c66af306d742376a",
            "meta": {},
            "score": 0.5312093733737563
        },
        "document_id": "30bbc99e952a511c66af306d742376a",
        "meta": {},
        "offsets_in_context": [
            {
                "end": 87,
                "start": 64
            }
        ],
        "offsets_in_document": [
            {
                "end": 96,
                "start": 73
            }
        ],
        "score": 0.3590219244360924,
        "type": "extractive"
    }
]

#print(answers[0]['document'])
answer_text = answers[0]['answer']
doc_content = answers[0]['document']['content']
sentences = nltk.tokenize.sent_tokenize(doc_content, language = 'spanish')
context = None
for sent in sentences:
    if answer_text in sent:
        context = sent
context = context.replace(answer_text, f"**{answer_text}**")
print(context)