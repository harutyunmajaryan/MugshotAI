import edge_tts
import subprocess


"""
The AI agent will process each suspect's profile and summarize the details audibly.
I developed this solution to streamline my workflow by replacing manual document review with automated text-to-speech presentation.
"""

async def speak(text):
    print("AI:", text)

    communicate = edge_tts.Communicate(
        text,
        "en-GB-RyanNeural"
    )

    player = subprocess.Popen(
        ["mpv", "--no-video", "--really-quiet", "-"],
        stdin=subprocess.PIPE
    )

    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            player.stdin.write(chunk["data"])

    player.stdin.close()
    player.wait()

