import curses

tasks = [
    {"title": "Learn Python", "done": False},
    {"title": "Build Task Manager", "done": False},
    {"title": "Push to GitHub", "done": False},
]

def draw_screen(stdscr, selected):
    stdscr.clear()

    stdscr.addstr(0, 0, "Mini Task Manager")
    stdscr.addstr(1, 0, "-" * 50)

    for i, task in enumerate(tasks):
        status = "[✓]" if task["done"] else "[ ]"
        line = f"{status} {task['title']}"

        if i == selected:
            stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(i + 3, 0, line)
            stdscr.attroff(curses.A_REVERSE)
        else:
            stdscr.addstr(i + 3, 0, line)

    stdscr.addstr(
        len(tasks) + 5,
        0,
        "↑↓ Navigate | Enter Toggle | a Add | d Delete | q Quit"
    )

    stdscr.refresh()


def add_task(stdscr):
    curses.echo()

    stdscr.clear()
    stdscr.addstr(0, 0, "Enter task name: ")
    task_name = stdscr.getstr().decode("utf-8")

    if task_name.strip():
        tasks.append({
            "title": task_name,
            "done": False
        })

    curses.noecho()


def main(stdscr):
    curses.curs_set(0)

    selected = 0

    while True:
        draw_screen(stdscr, selected)

        key = stdscr.getch()

        if key == curses.KEY_UP:
            selected = max(0, selected - 1)

        elif key == curses.KEY_DOWN:
            selected = min(len(tasks) - 1, selected + 1)

        elif key in [10, 13]:
            tasks[selected]["done"] = not tasks[selected]["done"]

        elif key == ord("a"):
            add_task(stdscr)

        elif key == ord("d"):
            if tasks:
                tasks.pop(selected)
                selected = max(0, selected - 1)

        elif key == ord("q"):
            break


curses.wrapper(main)