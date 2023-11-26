def do_replay(robot_name, silent=False):
    """
    Replays the movement commands from the command history and provides the full output or silent output.
    :param robot_name:
    :param silent: If True, only output the resulting position without showing each command.
    :return: (True, replay output text)
    """
    history = get_history()
    replayed_commands = 0
    original_commands = [cmd for cmd in history if cmd.split(' ')[0] in ['forward', 'back', 'left', 'right', 'sprint']]
    
    if not silent:
        for command in original_commands:
            handle_command(robot_name, command)
            replayed_commands += 1
    else:
        for command in original_commands:
            handle_command(robot_name, command)
            replayed_commands += 1
        return True, f" > {robot_name} replayed {replayed_commands} commands{' silently' if silent else ''}.\n > {robot_name} now at position {get_position(robot_name)}."
    
    for i in range(replayed_commands):
        history.pop()

    return True, f" > {robot_name} replayed {replayed_commands} commands{' silently' if silent else ''}."
