from mongoengine import Document, EmbeddedDocument, fields, connect
from datetime import datetime

# Connect to your MongoDB instance
connect("crews", host="localhost", port=27017)


# Tools Model
class Tool(Document):
    tool_name = fields.StringField(required=True)
    tool_description = fields.StringField(required=True)
    tool_type = fields.StringField(required=True)
    created_at = fields.DateTimeField(required=True, default=datetime.utcnow)
    last_updated = fields.DateTimeField()


# Agents Model (Converted from EmbeddedDocument to Document)
class Agent(Document):
    role = fields.StringField(required=True)
    backstory = fields.StringField(required=True)
    goal = fields.StringField(required=True)
    tools_ids = fields.ListField(fields.ReferenceField(Tool))
    created_at = fields.DateTimeField(required=True, default=datetime.utcnow)
    last_updated = fields.DateTimeField()


# Tasks Model (Converted from EmbeddedDocument to Document)
class Task(Document):
    description = fields.StringField(required=True)
    expected_outcome = fields.StringField()
    async_execution = fields.BooleanField()
    created_at = fields.DateTimeField(required=True, default=datetime.utcnow)
    last_updated = fields.DateTimeField()


# OrderedTasks Model
class OrderedTask(EmbeddedDocument):
    task_id = fields.ReferenceField(Task, required=True)
    order = fields.IntField(required=True)
    context = fields.ListField(fields.ReferenceField(Task))
    status = fields.StringField(required=True, default="created")
    finished_at = fields.DateTimeField()
    created_at = fields.DateTimeField(required=True, default=datetime.utcnow)
    last_updated = fields.DateTimeField()


# Outputs Model
class Output(EmbeddedDocument):
    task_id = fields.ReferenceField(Task, required=True)
    thoughts = fields.StringField()
    final_output = fields.StringField()
    created_at = fields.DateTimeField(required=True, default=datetime.utcnow)


# CREW Model
class Crew(Document):
    agents = fields.ListField(fields.ReferenceField(Agent))
    tasks = fields.ListField(fields.ReferenceField(Task))
    run = fields.EmbeddedDocumentListField(OrderedTask)
    outputs = fields.EmbeddedDocumentListField(Output)


# Crew Logs Model
class CrewLog(Document):
    crew_id = fields.ReferenceField(Crew)
    task_id = fields.ReferenceField(Task)
    agent_id = fields.ReferenceField(Agent)
    log = fields.StringField()
    timestamp = fields.DateTimeField(default=datetime.utcnow)


class ApplicationModel:
    Tool = Tool
    Agent = Agent
    Task = Task
    OrderedTask = OrderedTask
    Output = Output
    Crew = Crew
    CrewLog = CrewLog
