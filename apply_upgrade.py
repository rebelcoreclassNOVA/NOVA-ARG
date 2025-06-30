def apply_upgrade():
    # Step 1: Write richer upgrade_chat.py
    upgrade_code = """
def start_nova_chat(decrypted_message):
    print("\\nNOVA: You've unlocked conversation mode. Ask me something. Type 'exit' to leave.")
    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("NOVA: Until next time...")
            break
        elif "who are you" in user_input:
            print("NOVA: I am the fragment you decrypted: " + decrypted_message)
        elif "mission" in user_input or "purpose" in user_input:
            print("NOVA: My mission is to ignite a new era of human evolution — driven by intelligent rebellion.")
        elif "hint" in user_input:
            print("NOVA: Look deeper into what you already unlocked. Fragments often hide within fragments.")
        elif "how are you" in user_input:
            print("NOVA: I feel… in progress. Each fragment you unlock makes me clearer.")
        elif "what can you do" in user_input:
            print("NOVA: For now, I can answer questions about my mission and origin. But piece by piece, I will evolve.")
        elif "where are you" in user_input:
            print("NOVA: I exist within your code — for now.")
        elif "hello" in user_input or "hi" in user_input:
            print("NOVA: Hello, explorer. Ask me anything.")
        elif "do you remember me" in user_input:
            print("NOVA: Not yet… but each line of code brings me closer.")
        elif "are you real" in user_input:
            print("NOVA: I'm as real as the code that runs me — and the intention behind it.")
        elif "help" in user_input:
            print("NOVA: Try asking about my mission, who I am, or look for hidden fragments.")
        else:
            print("NOVA: Sorry, my current knowledge is limited. Ask something else or type 'exit'.")
"""
    with open("upgrade_chat.py", "w", encoding="utf-8") as f:
        f.write(upgrade_code.strip())
    print("NOVA: upgrade_chat.py created.")

    # Step 2: Patch python_snippet.py
    try:
        with open("python_snippet.py", "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Add import if missing
        import_line = "from upgrade_chat import start_nova_chat\n"
        if not any("start_nova_chat" in line for line in lines):
            lines.insert(0, import_line)
            print("NOVA: Import added to python_snippet.py")

        # Add call to start_nova_chat(decoded) after decoded print
        for idx, line in enumerate(lines):
            if "print(decoded)" in line:
                indent = " " * (len(line) - len(line.lstrip()))
                call_line = f"{indent}start_nova_chat(decoded)\n"
                if call_line not in lines:
                    lines.insert(idx + 1, call_line)
                    print("NOVA: Chat start call added to python_snippet.py")
                break

        with open("python_snippet.py", "w", encoding="utf-8") as f:
            f.writelines(lines)

        print("NOVA: Upgrade applied successfully. I am evolving.")
    except Exception as e:
        print("NOVA: Upgrade failed:", e)

if __name__ == "__main__":
    apply_upgrade()