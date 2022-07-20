from random import expovariate
import moviepy.editor as mpy
import sys

vcodec =   "libx264"

videoquality = "24"

# slow, ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
compression = "medium"

def concat_videos(loadtitles: list) -> any:
    print("[!] Concatenando videos...")
    videos = [] 
    for title in loadtitles:
        videos.append(mpy.VideoFileClip(title))
    concatenated = mpy.concatenate_videoclips(videos)
    export_video(concatenated, "concatenated.mp4")
    
def export_video(final_clip: any, savetitle: str) -> None:
    final_clip.write_videofile(savetitle, threads=4, fps=30,
                               codec=vcodec,
                               preset=compression,
                               ffmpeg_params=["-crf",videoquality])

def edit_video(loadtitle, savetitle, cuts):
    """ From: https://github.com/python-engineer/python-task-automation/blob/master/moviepy/edit.py """
    video = mpy.VideoFileClip(loadtitle)

    clips = []
    for cut in cuts:
        clip = video.subclip(cut[0], cut[1])
        clips.append(clip)

    final_clip = mpy.concatenate_videoclips(clips)
    
    export_video(final_clip, savetitle)

    video.close()


if __name__ == '__main__':
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("[!] Error en la ejecucion del comando. Debe ser `python3 edit.py video_name.mp4 00:01-00:02,")
        exit

    video_name = sys.argv[1]

    if "," in video_name:
        video_names = video_name.split(",")
        concat_videos(video_names)
    else:
        # The parts that we wanna keep
        cuts = [] # ('00:00:02.949', '00:00:04.152')
        cuts = [cut.split("-") for cut in sys.argv[2].split(",")]
        print(cuts)

        time_to = None
        try:
            time_to = sys.argv[3]
        except IndexError:
            pass

        edit_video(video_name, f"{video_name.replace('.mp4', '')}_editted.mp4", cuts)
