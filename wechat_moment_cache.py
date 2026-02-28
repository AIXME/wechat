# 朋友圈路径：/storage/emulated/0/Android/data/com.tencent.mm/cache/
# sns 文件夹里看到一堆像 snsb_3849xxxxxx的文件夹
'''步骤：
1. 微信刷朋友圈图片/视频，将媒体文件缓存
2. 获取微信朋友圈缓存目录
3. 遍历目录下文件：
   - 以 snshd 开头的文件 -> 添加 .jpg 后缀
   - 以 sight 开头的文件 -> 添加 .mp4 后缀
   - 其他文件保持原样
'''

import os
from pathlib import Path

def rename_cache_files(directory_path):
    """
    重命名缓存文件：
    1. snshd 开头的文件 -> .jpg
    2. sight 开头的文件 -> .mp4
    """
    path = Path(directory_path)
    
    # 确保路径存在
    if not path.exists():
        print(f"错误: 目录 '{directory_path}' 不存在")
        return

    # 获取脚本自身的文件名，避免重命名自己
    script_name = Path(__file__).name
    
    count = 0
    for file_path in path.iterdir():
        # 排除目录和脚本自身
        if not file_path.is_file() or file_path.name == script_name:
            continue

        name = file_path.name
        new_name = None

        # 1. snshd 开头的文件修改成 .jpg 后缀
        if name.startswith('snshd') and not name.lower().endswith('.jpg'):
            new_name = file_path.with_suffix(file_path.suffix + '.jpg')
        
        # 2. sight 开头的文件修改成 .mp4 后缀
        elif name.startswith('sight') and not name.lower().endswith('.mp4'):
            new_name = file_path.with_suffix(file_path.suffix + '.mp4')

        if new_name:
            try:
                file_path.rename(new_name)
                print(f"已重命名: {name} -> {new_name.name}")
                count += 1
            except Exception as e:
                print(f"重命名 {name} 失败: {e}")
                
    print(f"\n任务完成！共处理了 {count} 个文件。")

if __name__ == "__main__":
    # 使用当前目录
    current_dir = os.getcwd()
    print(f"开始处理目录: {current_dir}\n")
    rename_cache_files(current_dir)
