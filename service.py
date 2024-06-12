from datetime import datetime
from model import ApplicationModel


class ApplicationService(ApplicationModel):
    @classmethod
    def create_tool(cls, tool_name=None, tool_description=None, tool_type=None):
        tool = cls.Tool(
            tool_name=tool_name,
            tool_description=tool_description,
            tool_type=tool_type,
            created_at=datetime.utcnow(),
        )
        tool.save()
        return tool

    @classmethod
    def create_agent(cls, role=None, backstory=None, goal=None, tools_ids=None):
        agent = cls.Agent(
            role=role,
            backstory=backstory,
            goal=goal,
            tools_ids=tools_ids,
            created_at=datetime.utcnow(),
        )
        agent.save()
        return agent

    @classmethod
    def create_task(cls, description=None, expected_outcome=None, async_execution=None):
        task = cls.Task(
            description=description,
            expected_outcome=expected_outcome,
            async_execution=async_execution,
            created_at=datetime.utcnow(),
        )
        task.save()
        return task

    @classmethod
    def create_ordered_task(cls, task_id=None, order=None, context=None, status=None):
        ordered_task = cls.OrderedTask(
            task_id=task_id,
            order=order,
            context=context,
            status=status,
            created_at=datetime.utcnow(),
        )
        return ordered_task

    @classmethod
    def create_output(cls, task_id=None, thoughts=None, final_output=None):
        output = cls.Output(
            task_id=task_id,
            thoughts=thoughts,
            final_output=final_output,
            created_at=datetime.utcnow(),
        )
        return output

    @classmethod
    def create_crew(cls, agents=None, tasks=None, run=None, outputs=None):
        crew = cls.Crew(agents=agents, tasks=tasks, run=run, outputs=outputs)
        crew.save()
        return crew

    @classmethod
    def create_crew_log(cls, crew_id=None, task_id=None, agent_id=None, log=None):
        crew_log = cls.CrewLog(
            crew_id=crew_id,
            task_id=task_id,
            agent_id=agent_id,
            log=log,
            timestamp=datetime.utcnow(),
        )
        crew_log.save()
        return crew_log

    @classmethod
    def get_tool(cls, tool_id):
        return cls.Tool.objects(id=tool_id).first()

    @classmethod
    def get_agent(cls, agent_id):
        return cls.Agent.objects(id=agent_id).first()

    @classmethod
    def get_task(cls, task_id):
        return cls.Task.objects(id=task_id).first()

    @classmethod
    def get_ordered_task(cls, ordered_task_id):
        return cls.OrderedTask.objects(id=ordered_task_id).first()

    @classmethod
    def get_output(cls, output_id):
        return cls.Output.objects(id=output_id).first()

    @classmethod
    def get_crew(cls, crew_id):
        return cls.Crew.objects(id=crew_id).first()

    @classmethod
    def get_all_crews(cls):
        return cls.Crew.objects()

    @classmethod
    def get_crew_log(cls, crew_log_id):
        return cls.CrewLog.objects(id=crew_log_id).first()

    @classmethod
    def get_all_tools(cls):
        return cls.Tool.objects()

    @classmethod
    def get_all_agents(cls):
        return cls.Agent.objects()

    @classmethod
    def get_all_tasks(cls):
        return cls.Task.objects()

    @classmethod
    def get_all_ordered_tasks(cls):
        return cls.OrderedTask.objects()

    @classmethod
    def get_all_outputs(cls):
        return cls.Output.objects()

    @classmethod
    def get_all_crew_logs(cls):
        return cls.CrewLog.objects()

    @classmethod
    def update_tool(
        cls, tool_id, tool_name=None, tool_description=None, tool_type=None
    ):
        tool = cls.get_tool(tool_id)
        if tool:
            if tool_name is not None:
                tool.tool_name = tool_name
            if tool_description is not None:
                tool.tool_description = tool_description
            if tool_type is not None:
                tool.tool_type = tool_type
            tool.last_updated = datetime.utcnow()
            tool.save()
            return tool
        return None

    @classmethod
    def update_agent(cls, **kwargs):
        if "agent_id" not in kwargs.keys():
            return None
        agent_id = kwargs.get("agent_id")
        role = kwargs.get("role", "NOT_PRESENT")
        backstory = kwargs.get("backstory", None)
        goal = kwargs.get("goal", None)
        tools_ids = kwargs.get("tools_ids", None)
        agent = cls.get_agent(agent_id)
        if agent:
            if role is not None:
                agent.role = role
            if backstory is not None:
                agent.backstory = backstory
            if goal is not None:
                agent.goal = goal
            if tools_ids is not None:
                agent.tools_ids = tools_ids
            agent.last_updated = datetime.utcnow()
            agent.save()
            return agent
        return None

    @classmethod
    def update_task(
        cls, task_id, description=None, expected_outcome=None, async_execution=None
    ):
        task = cls.get_task(task_id)
        if task:
            if description is not None:
                task.description = description
            if expected_outcome is not None:
                task.expected_outcome = expected_outcome
            if async_execution is not None:
                task.async_execution = async_execution
            task.last_updated = datetime.utcnow()
            task.save()
            return task
        return None

    @classmethod
    def update_ordered_task(
        cls, ordered_task_id, task_id=None, order=None, context=None, status=None
    ):
        ordered_task = cls.get_ordered_task(ordered_task_id)
        if ordered_task:
            if task_id is not None:
                ordered_task.task_id = task_id
            if order is not None:
                ordered_task.order = order
            if context is not None:
                ordered_task.context = context
            if status is not None:
                ordered_task.status = status
            ordered_task.last_updated = datetime.utcnow()
            ordered_task.save()
            return ordered_task
        return None

    @classmethod
    def update_output(cls, output_id, task_id=None, thoughts=None, final_output=None):
        output = cls.get_output(output_id)
        if output:
            if task_id is not None:
                output.task_id = task_id
            if thoughts is not None:
                output.thoughts = thoughts
            if final_output is not None:
                output.final_output = final_output
            output.last_updated = datetime.utcnow()
            output.save()
            return output
        return None

    @classmethod
    def update_crew(cls, crew_id, agents=None, tasks=None, run=None, outputs=None):
        crew = cls.get_crew(crew_id)
        if crew:
            if agents is not None:
                crew.agents = agents
            if tasks is not None:
                crew.tasks = tasks
            if run is not None:
                crew.run = run
            if outputs is not None:
                crew.outputs = outputs
            crew.last_updated = datetime.utcnow()
            crew.save()
            return crew
        return None

    @classmethod
    def update_crew_log(
        cls, crew_log_id, crew_id=None, task_id=None, agent_id=None, log=None
    ):
        crew_log = cls.get_crew_log(crew_log_id)
        if crew_log:
            if crew_id is not None:
                crew_log.crew_id = crew_id
            if task_id is not None:
                crew_log.task_id = task_id
            if agent_id is not None:
                crew_log.agent_id = agent_id
            if log is not None:
                crew_log.log = log
            crew_log.last_updated = datetime.utcnow()
            crew_log.save()
            return crew_log
        return None

    @classmethod
    def delete_tool(cls, tool_id):
        tool = cls.get_tool(tool_id)
        if tool:
            tool.delete()
            return tool
        return None

    @classmethod
    def delete_agent(cls, agent_id):
        agent = cls.get_agent(agent_id)
        if agent:
            agent.delete()
            return agent
        return None

    @classmethod
    def delete_task(cls, task_id):
        task = cls.get_task(task_id)
        if task:
            task.delete()
            return task
        return None

    @classmethod
    def delete_ordered_task(cls, ordered_task_id):
        ordered_task = cls.get_ordered_task(ordered_task_id)
        if ordered_task:
            ordered_task.delete()
            return ordered_task
        return None

    @classmethod
    def delete_output(cls, output_id):
        output = cls.get_output(output_id)
        if output:
            output.delete()
            return output
        return None

    @classmethod
    def delete_crew(cls, crew_id):
        crew = cls.get_crew(crew_id)
        if crew:
            crew.delete()
            return crew
        return None

    @classmethod
    def delete_crew_log(cls, crew_log_id):
        crew_log = cls.get_crew_log(crew_log_id)
        if crew_log:
            crew_log.delete()
            return crew_log
        return None

    @classmethod
    def delete_all_tools(cls):
        return cls.Tool.objects().delete()

    @classmethod
    def delete_all_agents(cls):
        return cls.Agent.objects().delete()

    @classmethod
    def delete_all_tasks(cls):
        return cls.Task.objects().delete()

    @classmethod
    def delete_all_ordered_tasks(cls):
        return cls.OrderedTask.objects().delete()

    @classmethod
    def delete_all_outputs(cls):
        return cls.Output.objects().delete()

    @classmethod
    def delete_all_crews(cls):
        return cls.Crew.objects().delete()

    @classmethod
    def delete_all_crew_logs(cls):
        return cls.CrewLog.objects().delete()

    @classmethod
    def get_crew_with_nested_values(cls, crew_id):
        crew = cls.get_crew(crew_id)
        if crew:
            crew.agents = [
                agent.to_json() for agent in cls.Agent.objects(id__in=crew.agents)
            ]
            crew.tasks = [
                task.to_json() for task in cls.Task.objects(id__in=crew.tasks)
            ]
            crew.outputs = [output.to_json() for output in crew.outputs]
            crew.run = [ordered_task.to_json() for ordered_task in crew.run]
            return crew.to_json()
        return None

    class RequiredFieldsMissing(Exception):
        def __init__(self, required_fields: list[str]):
            self.message = f"Required fields are missing: {','.join(required_fields)}"
            super().__init__(self.message)
