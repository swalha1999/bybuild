# import subprocess
# import time
# from colorama import Fore, Back, Style
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler

# last_trigger_time = time.time()

# class MyHandler(FileSystemEventHandler):
#     def on_modified(self, event):
#         # global last_trigger_time
#         # current_time = time.time()
#         # if event.src_path.find('~') == -1 and (current_time - last_trigger_time) > 1:
#         #     last_trigger_time = current_time
#             if event.src_path.endswith('.c'):
#                 hot_reload(event.src_path)

# def compile_c_program(file_path):
#     try:
#         subprocess.check_output(['gcc', file_path, '-o', 'output'])
#         print(Fore.GREEN + "Compilation successful!" + Fore.RESET)
#     except subprocess.CalledProcessError as e:
#         print(Fore.RED + "Compilation failed" + Fore.RESET)

# def run_c_program():
#     try:
#         out = subprocess.check_output(['./output'])
#         # Decode the output
#         out = out.decode('utf-8')
#         print(out)
#     except subprocess.CalledProcessError as e:
#         print(Fore.RED+"Program failed:", e.output + Fore.RESET)

# def hot_reload(file_path):
#     print("Hot reloading:", file_path)
#     compile_c_program(file_path)
#     run_c_program()
    
    

# if __name__ == "__main__":
#     file_path = "test_program.c"
#     hot_reload(file_path)
#     path = '.'
#     event_handler = MyHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path, recursive=True)
#     observer.start()
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()

import os
import subprocess
import demoProject 
import demoProject2

def check_if_build_folder_exists():
    if not os.path.exists('build'):
        os.mkdir('build')

if __name__ == "__main__":
    
    demoProject.build()
    demoProject2.build()

    demoProject.run()
    demoProject2.run()