from flask import Flask, render_template_string, request, redirect, url_for
import json
import os

app = Flask(__name__)

FILE_NAME = "tasks.json"

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Moonlight Task Arcade</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            color: #4c2558;
            font-family: "Courier New", monospace;
            background-color: #f9c6df;
            background-image:
                radial-gradient(#ffffff 1px, transparent 1px),
                radial-gradient(#eaa1c7 1px, transparent 1px);
            background-size: 24px 24px;
            background-position: 0 0, 12px 12px;
        }

        .page {
            width: min(1000px, 92%);
            margin: auto;
            padding: 35px 0 60px;
        }

        .window {
            background: #fff6fb;
            border: 5px solid #743d8a;
            box-shadow: 10px 10px 0 #d981b1;
        }

        .top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 22px;
            color: #fff6fb;
            background: #743d8a;
        }

        .logo {
            font-size: 23px;
            font-weight: bold;
            letter-spacing: 1px;
        }

        .level {
            padding: 8px 12px;
            color: #743d8a;
            background: #ffd55c;
            border: 3px solid #fff6fb;
            font-weight: bold;
        }

        .hero {
            padding: 30px;
            text-align: center;
            background: linear-gradient(135deg, #ffb8d7, #d6b4f4);
            border-bottom: 5px solid #743d8a;
        }

        .hero h1 {
            margin: 0;
            font-size: clamp(30px, 5vw, 48px);
            color: #6b317c;
            text-shadow: 3px 3px 0 #fff6fb;
        }

        .hero p {
            margin-bottom: 0;
            font-weight: bold;
        }

        .content {
            padding: 28px;
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
            margin-bottom: 28px;
        }

        .stat {
            padding: 16px;
            text-align: center;
            background: #ffe7f2;
            border: 3px solid #bc6fa4;
            box-shadow: 4px 4px 0 #f3a2c8;
        }

        .stat-number {
            display: block;
            font-size: 29px;
            font-weight: bold;
            color: #773c8a;
        }

        h2 {
            font-size: 21px;
            color: #743d8a;
        }

        .add-form {
            display: grid;
            grid-template-columns: 1fr 160px 140px;
            gap: 10px;
            margin-bottom: 28px;
        }

        input, select, button {
            padding: 13px;
            border: 3px solid #a95893;
            font-family: "Courier New", monospace;
            font-size: 14px;
        }

        input, select {
            color: #4c2558;
            background: white;
        }

        button {
            color: white;
            background: #d65093;
            box-shadow: 4px 4px 0 #743d8a;
            font-weight: bold;
            cursor: pointer;
        }

        button:hover {
            background: #ef6bac;
        }

        button:active {
            transform: translate(3px, 3px);
            box-shadow: 1px 1px 0 #743d8a;
        }

        .task-list {
            display: grid;
            gap: 14px;
        }

        .task {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 18px;
            padding: 18px;
            background: #fff;
            border: 3px solid #bc6fa4;
            box-shadow: 5px 5px 0 #f1b0d0;
        }

        .task.done {
            opacity: .65;
            background: #eee0f5;
        }

        .task-title {
            margin: 0 0 8px;
            font-size: 17px;
            font-weight: bold;
        }

        .done .task-title {
            text-decoration: line-through;
        }

        .task-details {
            font-size: 13px;
            color: #774a70;
        }

        .badge {
            display: inline-block;
            margin-top: 10px;
            padding: 5px 8px;
            color: #fff;
            background: #8d5dab;
            font-size: 12px;
            font-weight: bold;
        }

        .priority-high {
            background: #d65074;
        }

        .priority-medium {
            background: #c07a36;
        }

        .priority-low {
            background: #579276;
        }

        .task-actions {
            display: flex;
            gap: 9px;
        }

        .delete-button {
            background: #9c4f78;
        }

        .empty {
            padding: 30px;
            text-align: center;
            color: #7c477b;
            background: #ffe7f2;
            border: 3px dashed #bc6fa4;
        }

        .progress-box {
            margin-top: 28px;
            padding: 18px;
            background: #efe0f7;
            border: 3px solid #8d5dab;
        }

        .progress-bar {
            height: 24px;
            overflow: hidden;
            background: white;
            border: 3px solid #743d8a;
        }

        .progress {
            height: 100%;
            background: linear-gradient(90deg, #ef6bac, #ffd55c);
        }

        @media (max-width: 720px) {
            .top-bar, .task {
                align-items: flex-start;
                flex-direction: column;
            }

            .stats, .add-form {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>

<body>
    <main class="page">
        <section class="window">
            <header class="top-bar">
                <div class="logo">MOONLIGHT TASK ARCADE</div>
                <div class="level">LEVEL {{ level }} PLAYER</div>
            </header>

            <section class="hero">
                <h1>Study Quest</h1>
                <p>Organize your missions. Gain XP. Level up.</p>
            </section>

            <section class="content">
                <section class="stats">
                    <div class="stat">
                        <span class="stat-number">{{ xp }}</span>
                        MAGIC XP
                    </div>
                    <div class="stat">
                        <span class="stat-number">{{ completed }}</span>
                        QUESTS WON
                    </div>
                    <div class="stat">
                        <span class="stat-number">{{ tasks|length }}</span>
                        TOTAL QUESTS
                    </div>
                </section>

                <h2>NEW QUEST</h2>

                <form class="add-form" action="/add" method="POST">
                    <input name="title" placeholder="What is your next task?" required>
                    <select name="priority">
                        <option value="Low">Low priority</option>
                        <option value="Medium" selected>Medium priority</option>
                        <option value="High">High priority</option>
                    </select>
                    <button type="submit">ADD QUEST</button>
                </form>

                <h2>QUEST BOARD</h2>

                <section class="task-list">
                    {% if tasks %}
                        {% for task in tasks %}
                            <article class="task {% if task.done %}done{% endif %}">
                                <div>
                                    <p class="task-title">{{ task.title }}</p>
                                    <p class="task-details">Reward: 25 XP</p>
                                    <span class="badge priority-{{ task.priority|lower }}">
                                        {{ task.priority }} PRIORITY
                                    </span>
                                </div>

                                <div class="task-actions">
                                    <form action="/toggle/{{ loop.index0 }}" method="POST">
                                        <button type="submit">
                                            {% if task.done %}UNDO{% else %}COMPLETE{% endif %}
                                        </button>
                                    </form>

                                    <form action="/delete/{{ loop.index0 }}" method="POST">
                                        <button class="delete-button" type="submit">DELETE</button>
                                    </form>
                                </div>
                            </article>
                        {% endfor %}
                    {% else %}
                        <div class="empty">
                            Your quest board is empty. Add your first mission above.
                        </div>
                    {% endif %}
                </section>

                <section class="progress-box">
                    <h2>LEVEL PROGRESS</h2>
                    <p>{{ progress }} / 100 XP until the next level</p>
                    <div class="progress-bar">
                        <div class="progress" style="width: {{ progress }}%;"></div>
                    </div>
                </section>
            </section>
        </section>
    </main>
</body>
</html>
"""

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

@app.route("/")
def home():
    tasks = load_tasks()
    completed = sum(task["done"] for task in tasks)
    xp = completed * 25
    level = (xp // 100) + 1
    progress = xp % 100

    return render_template_string(
        TEMPLATE,
        tasks=tasks,
        completed=completed,
        xp=xp,
        level=level,
        progress=progress
    )

@app.route("/add", methods=["POST"])
def add_task():
    tasks = load_tasks()
    title = request.form["title"].strip()
    priority = request.form["priority"]

    if title:
        tasks.append({
            "title": title,
            "priority": priority,
            "done": False
        })
        save_tasks(tasks)

    return redirect(url_for("home"))

@app.route("/toggle/<int:task_index>", methods=["POST"])
def toggle_task(task_index):
    tasks = load_tasks()

    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = not tasks[task_index]["done"]
        save_tasks(tasks)

    return redirect(url_for("home"))

@app.route("/delete/<int:task_index>", methods=["POST"])
def delete_task(task_index):
    tasks = load_tasks()

    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        save_tasks(tasks)

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
