# logieminu
A program for modifying Korg Minilogue Sound Library files.

## File formats
The Korg Minilogue has the option to import and export programs to file via the Korg Minilogue Sound Librarian application. The application allows you to download sound libraries and send them to your Minilogue or to dump your existing programs to file.

Korg Minilogue Sound Librarian file formats are:
- mnlglib: Library data. Typically an export from a Minilogue
- mnlgprog: Program data: A single program
- mnlgpreset: A program collection. Typically downloaded from Korg or a third party patch designer

All three of these format have similar internal structure. They're all zip files containing one or more program binary (prog_bin) files plus XML metadata. By modifying the prog_bin files, we can adjust the program sounds.

## prog_bin format
The prog_bin file contains the sound program parameters as set by knobs and buttons on the Korg Minilogue. It is a fixed length (448 bytes) binary format.

A partial map of prog_bin showing the parameters they control. All values are hexadecimal unless stated otherwise.

| Offset              | Purpose      | Acceptable values                           | Default value |
|---------------------|--------------|---------------------------------------------|---------------|
| 00000000 - 00000003 | Constant     | "PROG"                                      | "PROG"        |
| 00000004 - 00000013 | Program name | Any alphanumeric and some special characters | Init Program  |
| 00000014            | VCO 1 Pitch | 00-FF | 80 |
| 00000015            | VCO 1 Shape | 00-FF | 00 |
| 00000016            | VCO 2 Pitch | 00-FF | 80 |
| 00000017            | VCO 2 Shape | 00-FF | 00 |
| 00000018            | Cross Mod | 00-FF | 00 |
| 00000019            | Pitch EG Int | 00-FF | 80 |
| 0000001A            | VCO 1 Mixer | 00-FF | FF |
| 0000001B            | VCO 2 Mixer | 00-FF | 00 |
| 0000001C            | Noise Mixer | 00-FF | 00 |
| 0000001D            | Filter Cutoff | 00-FF | FF |
| 0000001E            | Filter Resonance | 00-FF | 00 |
| 0000001F            | Filter EG Int | 00-FF | 80 |
| 00000022            | Amp EG Attack | 00-FF | 00 |
| 00000023            | Amp EG Decay | 00-FF | 80 |
| 00000024            | Amp EG Sustain | 00-FF | FF |
| 00000025            | Amp EG Release | 00-FF | 00 |
| 00000026            | EG Attack | 00-FF | 00 |
| 00000027            | EG Decay | 00-FF | 80 |
| 00000028            | EG Sustain | 00-FF | 00 |
| 00000029            | EG Release | 00-FF | 00 |
| 0000002A            | LFO Rate | 00-FF | 80 |
| 0000002B            | LFO Int | 00-FF | 00 |
| 00000031            | Delay Hipass cutoff | 00-FF | 40 |
| 00000032            | Delay time | 00-FF | FF |
| 00000033            | Delay feedback | 00-FF | 80 |
| 00000034            | VCO 1 Octave | 80-B0 | 90 |
| 00000034            | VCO 1 wave | 90:saw, 50:tri, 10:sqr | 90 |
| 00000035            | VCO 2 Octave | 80-B0 | 90 |
| 00000035            | VCO 2 wave | 90:saw, 50:tri, 10:sqr | 90 |
| 00000037            | Ring | 32:on, 30:off | 30 |
| 00000037            | Sync | 31:on, 30:off | 30 |
| 00000038            | 2-pole/4-pole | C0:2-pole, 80:4-pole | C0 |
| 00000038            | Key Track | E0:100%, D0:50%, C0:0% | C0 |
| 00000038            | Velocity | C8:100%, C4:50%, C0:0% | C0 |
| 0000003B            | LFO EG Mod | A0:int, 60:rate, 20:off | 20 |
| 0000003B            | LFO Target | 20:pitch, 10:shape, 00:cutoff | 20 |
| 0000003C            | Delay output routing | BD:post-filter, 7D:pre-filter, 3D:bypass | 3D |
| 0000003C            | LFO Wave | 3E:saw, 3D:tri, 3C;sqr | 3D |
| 00000040            | Arp mode | CE-FE | C8 |
| 00000040            | Chord mode | CC-FC | C8 |
| 00000040            | Delay mode | CD-FD | C8 |
| 00000040            | Duo mode detune | C9-F9 | C8 |
| 00000040            | Mono mode sub | CB-FB | C8 |
| 00000040            | Sidechain mode depth | CF-FF | C8 |
| 00000040            | Unison mode detune | CA-FA | C8 |
| 00000040            | Poly mode depth | C8-F8 | C8 |
| 00000049            | Master Octave | F8-FC | FA |
| 00000064            | Tempo | 30-60 | B0 |

Note that the byte at some offsets encode more than one setting. The byte at 0x00000040 in particular controls both the voice mode buttons and the voice mode depth knob.

Bytes beyond 0x00000060 control the sequencer and are out of scope of this application.


## Legal
This application is not affiliated or endorsed by Korg. It is provided "as is" without warranty of any kind. Any patches and programs created with this application are used at your own risk.
