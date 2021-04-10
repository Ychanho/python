from pytube import YouTube
import os
import json

# 파일 생성할 때 쓸 수 없는 문자 제거
def cln_txt(txt):
    delete_list = ['-', '(', ')', '|', '\\', '[', ']', '?']
    for i in range(len(delete_list)):
        txt = txt.replace(delete_list[i], '')

    return txt.replace(' ', '_').replace('/', '~').replace('“', '\'').replace('”', '\'')
    # return txt.replace('-', '').replace(' ', '_').replace('/', '~').replace('(', '').replace(')', '').replace('|', '').replace('\\', '').replace('“', '\'').replace('”', '\'').replace('[', '').replace(']', '')

def download_data(url, v_type='video/mp4', res=['1080p', '720p', '360p']):
    crawl_result = {'url': url}
    yt = YouTube(url)
    # streams = yt.streams  # 소리 없이 영상만 다운 됨
    streams = yt.streams.filter(progressive=True).all()
    # yt.streams.filter(only_audio=True).all()  # 음원 다운
    for i, stream in enumerate(streams):
        print(i, stream)

    import sys
    sys.exit()

    crawl_result['title'] = yt.title

    folder_name = cln_txt(yt.title)
    target_folder = os.path.join('data', folder_name)

    if not os.path.exists(target_folder):   # 경로가 없으면 만들기
        os.makedirs(target_folder)

    targets = list()

    for item in streams:
        if item.resolution in res and item.mime_type == v_type:
            targets.append(item)

    res_cache = {'1080p': False, '720p': False, '360p': False}

    for target in targets:  # resolution(해상도)
        video_info = {'resolution': target.resolution,
                      'mime_type': target.mime_type,
                      'fps': target.fps}
        vid_path = os.path.join(target_folder, target.resolution)

        if res_cache[target.resolution] == True:
            continue
        try:
            os.mkdir(vid_path)
        except FileExistsError:
            pass

        target.download(vid_path)

        with open(os.path.join(vid_path, 'video_info.json'), 'w') as f:
            json.dump(video_info, f)

    captions = yt.caption_tracks
    subt_folder = os.path.join(target_folder, 'subtitles')
    os.mkdir(subt_folder)
    for caption in captions:
        text = caption.generate_srt_captions()
        with open(os.path.join(subt_folder, caption.code + '_' + cln_txt(caption.name) + '.txt'), 'w', encoding='utf8') as f:
            f.write(text)

    return yt.title, True


if __name__ == "__main__":

    url = "https://www.youtube.com/watch?v=mFzyyD7fkug&t=124s&ab_channel=MYPLAYLIST" #가져올 링크
    try:
        title, is_ok = download_data(url)
    except Exception as e:
        print(str(e))
        print(url)
        print()