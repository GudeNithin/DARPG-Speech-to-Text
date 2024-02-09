{ pkgs }: {
  deps = [
    pkgs.jellyfin-ffmpeg.bin
    pkgs.ffmpeg_6-full.bin
  ];
}