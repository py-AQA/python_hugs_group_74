-- CREATE DATABASE my_db COLLATE utf8_unicode_ci;

CREATE TABLE IF NOT EXISTS topics
(
    id   INT AUTO_INCREMENT, -- Идентификатор темы
    name VARCHAR(256) NOT NULL COMMENT 'Название темы',
    CONSTRAINT topics_pk
        PRIMARY KEY (id)
)
    COMMENT 'Тема';

INSERT INTO topics (id, name)
VALUES (1, 'SQL'),
       (2, 'Python'),
       (3, 'Тест-дизайн'),
       (4, 'Свободная тема');

CREATE TABLE IF NOT EXISTS question_types
(
    id              VARCHAR(20), -- Идентификатор типа вопроса
    name            VARCHAR(256) NOT NULL COMMENT 'Название типа вопроса',
    automatic_check BOOLEAN      NOT NULL DEFAULT FALSE COMMENT 'Автоматическая проверка или человеком?',
    CONSTRAINT question_types_pk
        PRIMARY KEY (id)
)
    COMMENT 'Тип вопроса';

-- Тип вопроса - определение (текст)
-- и решить практическую задачу (составить запрос или программу),
-- или выбор из предложенного варианта = Тип ответа
-- Может быть вопрос где надо выбрать несколько вариантов ответа

INSERT INTO question_types (id, name, automatic_check)
VALUES ('text', 'Текстовый вопрос', FALSE),
       ('task', 'Задача (составить запрос или программу)', FALSE),
       ('choice', 'Выбор варианта', TRUE),
       ('multiple_choice', 'Выбрать несколько вариантов', TRUE);

-- Вопрос (Задача) - задание
-- Сложность - Junior, Middle, Senior
-- Возможна ссылка на предыдущий и следующий вопросы
-- Количество баллов
-- Текст вопроса
CREATE TABLE IF NOT EXISTS questions
(
    id            INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Идентификатор вопроса',
    topic_id      INT                                 NOT NULL COMMENT 'Идентификатор темы',
    FOREIGN KEY (topic_id) REFERENCES topics (id),
    text          TEXT                                NOT NULL COMMENT 'Текст вопроса',
    question_type VARCHAR(20)                         NOT NULL COMMENT 'Тип вопроса',
    FOREIGN KEY (question_type) REFERENCES question_types (id),
    difficulty    ENUM ('Junior', 'Middle', 'Senior') NOT NULL COMMENT 'Сложность',
    points        INT                                 NOT NULL COMMENT 'Количество баллов',
    prev_id       INT                                 NULL DEFAULT NULL COMMENT 'Предыдущий вопрос',
    FOREIGN KEY (prev_id) REFERENCES questions (id),
    next_id       INT                                 NULL DEFAULT NULL COMMENT 'Следующий вопрос',
    FOREIGN KEY (next_id) REFERENCES questions (id)
) COMMENT 'Вопрос (Задача) - задание';

-- Укажите верное утверждение:
INSERT INTO questions
    (id, topic_id, text, question_type, difficulty, points)
VALUES (1, 1, 'Укажите верное утверждение:', 'choice', 'Junior', 10);

-- Вариант 1
-- сценарий mysqlbug составляет отчет о возникшей в MySQL неполадке
-- Вариант 2
-- сценарий mysqlbug проверяет двоичный журнал на наличие ошибок
-- Вариант 3
-- сценарий mysqlsend может использоваться для составления отчета для почтового списка рассылки MySQL
CREATE TABLE IF NOT EXISTS answer_variants
(
    question_id INT     NOT NULL COMMENT 'Вопрос',
    FOREIGN KEY (question_id) REFERENCES questions (id) ON DELETE CASCADE,
    no          INT     NOT NULL DEFAULT 1 COMMENT '',
    text        TEXT    NOT NULL COMMENT 'Текст варианта',
    is_right    BOOLEAN NOT NULL COMMENT 'Это правильный ответ?',
    CONSTRAINT answer_variants_pk
        PRIMARY KEY (question_id, no)
) COMMENT 'Варианты ответов';

INSERT INTO answer_variants
    (question_id, no, text, is_right)
VALUES (1, 1,
        'сценарий mysqlbug составляет отчет о возникшей в MySQL неполадке',
        TRUE),
       (1, 2, 'сценарий mysqlbug проверяет двоичный журнал на наличие ошибок',
        FALSE),
       (1, 3, 'сценарий mysqlsend может использоваться для составления отчета для почтового списка рассылки MySQL',
        FALSE);

