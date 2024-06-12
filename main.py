from flask import Flask, request, jsonify
from service import ApplicationService

app = Flask(__name__)


# Endpoints for Tools
@app.route("/tools", methods=["POST"])
def create_tool():
    data = request.json
    tool = ApplicationService.create_tool(
        tool_name=data.get("tool_name"),
        tool_description=data.get("tool_description"),
        tool_type=data.get("tool_type"),
    )
    return jsonify(tool.to_json()), 201


@app.route("/tools/<tool_id>", methods=["GET"])
def get_tool(tool_id):
    tool = ApplicationService.get_tool(tool_id)
    if tool:
        return jsonify(tool.to_json()), 200
    return jsonify({"error": "Tool not found"}), 404


@app.route("/tools", methods=["GET"])
def get_all_tools():
    tools = ApplicationService.get_all_tools()
    return jsonify([tool.to_json() for tool in tools]), 200


@app.route("/tools/<tool_id>", methods=["PUT"])
def update_tool(tool_id):
    data = request.json
    tool = ApplicationService.update_tool(
        tool_id,
        tool_name=data.get("tool_name"),
        tool_description=data.get("tool_description"),
        tool_type=data.get("tool_type"),
    )
    if tool:
        return jsonify(tool.to_json()), 200
    return jsonify({"error": "Tool not found"}), 404


@app.route("/tools/<tool_id>", methods=["DELETE"])
def delete_tool(tool_id):
    tool = ApplicationService.delete_tool(tool_id)
    if tool:
        return jsonify({"success": "Tool deleted"}), 200
    return jsonify({"error": "Tool not found"}), 404


# Endpoints for Agents
@app.route("/agents", methods=["POST"])
def create_agent():
    data = request.json
    agent = ApplicationService.create_agent(
        role=data.get("role"),
        backstory=data.get("backstory"),
        goal=data.get("goal"),
        tools_ids=data.get("tools_ids"),
    )
    return jsonify(agent.to_json()), 201


@app.route("/agents/<agent_id>", methods=["GET"])
def get_agent(agent_id):
    agent = ApplicationService.get_agent(agent_id)
    if agent:
        return jsonify(agent.to_json()), 200
    return jsonify({"error": "Agent not found"}), 404


@app.route("/agents", methods=["GET"])
def get_all_agents():
    agents = ApplicationService.get_all_agents()
    return jsonify([agent.to_json() for agent in agents]), 200


@app.route("/agents/<agent_id>", methods=["PUT"])
def update_agent(agent_id):
    data = request.json
    agent = ApplicationService.update_agent(
        agent_id,
        role=data.get("role"),
        backstory=data.get("backstory"),
        goal=data.get("goal"),
        tools_ids=data.get("tools_ids"),
    )
    if agent:
        return jsonify(agent.to_json()), 200
    return jsonify({"error": "Agent not found"}), 404


@app.route("/agents/<agent_id>", methods=["DELETE"])
def delete_agent(agent_id):
    agent = ApplicationService.delete_agent(agent_id)
    if agent:
        return jsonify({"success": "Agent deleted"}), 200
    return jsonify({"error": "Agent not found"}), 404


# Endpoints for Tasks
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    task = ApplicationService.create_task(
        description=data.get("description"),
        expected_outcome=data.get("expected_outcome"),
        async_execution=data.get("async_execution"),
    )
    return jsonify(task.to_json()), 201


@app.route("/tasks/<task_id>", methods=["GET"])
def get_task(task_id):
    task = ApplicationService.get_task(task_id)
    if task:
        return jsonify(task.to_json()), 200
    return jsonify({"error": "Task not found"}), 404


@app.route("/tasks", methods=["GET"])
def get_all_tasks():
    tasks = ApplicationService.get_all_tasks()
    return jsonify([task.to_json() for task in tasks]), 200


@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.json
    task = ApplicationService.update_task(
        task_id,
        description=data.get("description"),
        expected_outcome=data.get("expected_outcome"),
        async_execution=data.get("async_execution"),
    )
    if task:
        return jsonify(task.to_json()), 200
    return jsonify({"error": "Task not found"}), 404


@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = ApplicationService.delete_task(task_id)
    if task:
        return jsonify({"success": "Task deleted"}), 200
    return jsonify({"error": "Task not found"}), 404


# Endpoints for OrderedTasks
@app.route("/ordered_tasks", methods=["POST"])
def create_ordered_task():
    data = request.json
    ordered_task = ApplicationService.create_ordered_task(
        task_id=data.get("task_id"),
        order=data.get("order"),
        context=data.get("context"),
        status=data.get("status"),
    )
    return jsonify(ordered_task.to_json()), 201


@app.route("/ordered_tasks/<ordered_task_id>", methods=["GET"])
def get_ordered_task(ordered_task_id):
    ordered_task = ApplicationService.get_ordered_task(ordered_task_id)
    if ordered_task:
        return jsonify(ordered_task.to_json()), 200
    return jsonify({"error": "Ordered task not found"}), 404


@app.route("/ordered_tasks", methods=["GET"])
def get_all_ordered_tasks():
    ordered_tasks = ApplicationService.get_all_ordered_tasks()
    return jsonify([ordered_task.to_json() for ordered_task in ordered_tasks]), 200


@app.route("/ordered_tasks/<ordered_task_id>", methods=["PUT"])
def update_ordered_task(ordered_task_id):
    data = request.json
    ordered_task = ApplicationService.update_ordered_task(
        ordered_task_id,
        task_id=data.get("task_id"),
        order=data.get("order"),
        context=data.get("context"),
        status=data.get("status"),
    )
    if ordered_task:
        return jsonify(ordered_task.to_json()), 200
    return jsonify({"error": "Ordered task not found"}), 404


@app.route("/ordered_tasks/<ordered_task_id>", methods=["DELETE"])
def delete_ordered_task(ordered_task_id):
    ordered_task = ApplicationService.delete_ordered_task(ordered_task_id)
    if ordered_task:
        return jsonify({"success": "Ordered task deleted"}), 200
    return jsonify({"error": "Ordered task not found"}), 404


# Endpoints for Outputs
@app.route("/outputs", methods=["POST"])
def create_output():
    data = request.json
    output = ApplicationService.create_output(
        task_id=data.get("task_id"),
        thoughts=data.get("thoughts"),
        final_output=data.get("final_output"),
    )
    if output:
        return jsonify(output.to_json()), 201
    return jsonify({"error": "Task not found"}), 404


@app.route("/outputs/<output_id>", methods=["GET"])
def get_output(output_id):
    output = ApplicationService.get_output(output_id)
    if output:
        return jsonify(output.to_json()), 200
    return jsonify({"error": "Output not found"}), 404


@app.route("/outputs", methods=["GET"])
def get_all_outputs():
    outputs = ApplicationService.get_all_outputs()
    if outputs:
        return jsonify([output.to_json() for output in outputs]), 200
    return jsonify({"error": "No outputs found"}), 404


@app.route("/outputs/<output_id>", methods=["PUT"])
def update_output(output_id):
    data = request.json
    output = ApplicationService.update_output(
        output_id,
        task_id=data.get("task_id"),
        thoughts=data.get("thoughts"),
        final_output=data.get("final_output"),
    )
    if output:
        return jsonify(output.to_json()), 200
    return jsonify({"error": "Output not found"}), 404


@app.route("/outputs/<output_id>", methods=["DELETE"])
def delete_output(output_id):
    output = ApplicationService.delete_output(output_id)
    if output:
        return jsonify({"success": "Output deleted"}), 200
    return jsonify({"error": "Output not found"}), 404


# Endpoints for Crew
@app.route("/crew", methods=["POST"])
def create_crew():
    data = request.json
    crew = ApplicationService.create_crew(
        agents=data.get("agents"),
        tasks=data.get("tasks"),
        run=data.get("run"),
        outputs=data.get("outputs"),
    )
    return jsonify(crew.to_json()), 201


@app.route("/crew/<crew_id>", methods=["GET"])
def get_crew(crew_id):
    crew = ApplicationService.get_crew_with_nested_values(crew_id)
    if crew:
        return jsonify(crew.to_json()), 200
    return jsonify({"error": "Crew not found"}), 404


@app.route("/crews", methods=["GET"])
def get_all_crews():
    crews = ApplicationService.get_all_crews()
    return jsonify([crew.to_json() for crew in crews]), 200


@app.route("/crew/<crew_id>", methods=["PUT"])
def update_crew(crew_id):
    data = request.json
    crew = ApplicationService.update_crew(
        crew_id,
        agents=data.get("agents"),
        tasks=data.get("tasks"),
        run=data.get("run"),
        outputs=data.get("outputs"),
    )
    if crew:
        return jsonify(crew.to_json()), 200
    return jsonify({"error": "Crew not found"}), 404


@app.route("/crew/<crew_id>", methods=["DELETE"])
def delete_crew(crew_id):
    crew = ApplicationService.delete_crew(crew_id)
    if crew:
        return jsonify({"success": "Crew deleted"}), 200
    return jsonify({"error": "Crew not found"}), 404


# Endpoints for CrewLogs
@app.route("/crew_logs", methods=["POST"])
def create_crew_log():
    data = request.json
    crew_log = ApplicationService.create_crew_log(
        crew_id=data.get("crew_id"),
        task_id=data.get("task_id"),
        agent_id=data.get("agent_id"),
        log=data.get("log"),
    )
    return jsonify(crew_log.to_json()), 201


@app.route("/crew_logs/<crew_log_id>", methods=["GET"])
def get_crew_log(crew_log_id):
    crew_log = ApplicationService.get_crew_log(crew_log_id)
    if crew_log:
        return jsonify(crew_log.to_json()), 200
    return jsonify({"error": "Crew log not found"}), 404


@app.route("/crew_logs", methods=["GET"])
def get_all_crew_logs():
    crew_logs = ApplicationService.get_all_crew_logs()
    return jsonify([crew_log.to_json() for crew_log in crew_logs]), 200


@app.route("/crew_logs/<crew_log_id>", methods=["PUT"])
def update_crew_log(crew_log_id):
    data = request.json
    crew_log = ApplicationService.update_crew_log(
        crew_log_id,
        crew_id=data.get("crew_id"),
        task_id=data.get("task_id"),
        agent_id=data.get("agent_id"),
        log=data.get("log"),
    )
    if crew_log:
        return jsonify(crew_log.to_json()), 200
    return jsonify({"error": "Crew log not found"}), 404


@app.route("/crew_logs/<crew_log_id>", methods=["DELETE"])
def delete_crew_log(crew_log_id):
    crew_log = ApplicationService.delete_crew_log(crew_log_id)
    if crew_log:
        return jsonify({"success": "Crew log deleted"}), 200
    return jsonify({"error": "Crew log not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
