# Boom Board

A 27-pad meme sound board in a single web page. Tap a pad to play its sound, and tap it again to stop. Different pads can play at the same time.

## Use it

**Online:** https://thad-the-impaler.github.io/Sound-Board/ works on any phone or computer.

**Offline:** download or clone the repo and open **`index.html`** in a browser. Every sound is built into that one file, so it works from any folder and needs no server or internet connection.

- **Mouse or touch:** tap a pad to play it, and tap a playing pad to stop it.
- **Keyboard:** each pad shows its key (`1`–`0`, then letters from `q`). `Esc` stops everything.
- **Master** sets the volume for all pads. **Stop all** stops every sound.
- On an iPhone, turn off the silent switch if you hear nothing.

## Files

| Path | What it is |
| --- | --- |
| `index.html` | The board with all sounds built in. Open this one. Generated; don't edit it by hand. |
| `board.html` | The page source. It loads sounds from `sounds/`, so it needs a web server. |
| `sounds/` | The 27 trimmed clips (MP3, 192 kbps). |
| `tools/build_index.py` | Rebuilds `index.html` from `board.html` and `sounds/`. |

After changing `board.html` or a clip, rebuild:

```bash
python3 tools/build_index.py
```

To add a pad, add the clip to `sounds/<id>.mp3`, add an entry with that `id` to `BANKS` in `board.html`, then rebuild.

## Sounds

Clips are trimmed to the moment itself and loudness-matched. Speech is about −16 LUFS. Crickets, the romantic music and the screams are a little quieter so they don't overpower everything else.

| Pad | Key | Source | Clip taken from |
| --- | --- | --- | --- |
| Buzzer | 1 | Wrong-answer buzzer | [YouTube](https://www.youtube.com/watch?v=2naim9F4010) 0:01.7–0:02.9 |
| Ding Ding | 2 | Correct-answer ding | [YouTube](https://www.youtube.com/watch?v=boaUpTtZUgA) 0:01.8–0:03.0 |
| Sitcom Laughter | 3 | Studio audience | [YouTube](https://www.youtube.com/watch?v=4VTBMznLrWs) 0:00.1–0:06.4 |
| Crickets | 4 | Awkward silence | [YouTube](https://www.youtube.com/watch?v=CpGtBnVZLSk) 0:00.0–0:06.5 |
| Womp Womp | 5 | Sad trombone | [YouTube](https://www.youtube.com/watch?v=CQeezCdF4mk) 0:00.3–0:03.9 |
| Romantic Music | 6 | Romantic sax meme track | [YouTube](https://www.youtube.com/watch?v=1GKjilVJuf8) 0:00.3–0:11.0 |
| Vine Boom | 7 | Vine boom | [YouTube](https://www.youtube.com/watch?v=Oc7Cin_87H4) 0:00.2–0:03.1 |
| Among Us Stinger | 8 | Among Us role reveal | [YouTube](https://www.youtube.com/watch?v=ekL881PJMjI) 0:00.1–0:04.3 |
| The Missile Knows Where It Is | 9 | Missile guidance training film narration | [YouTube](https://www.youtube.com/watch?v=bZe5J8SVCYQ) 0:02.6–0:08.1 |
| Oh No It All Went Wrong | 0 | *Chowder* | [YouTube](https://www.youtube.com/watch?v=TIZneWRGxZ8) 0:02.2–0:07.7 |
| Wilhelm Scream | q | *Distant Drums* (1951), take 4 of the original session | [YouTube](https://www.youtube.com/watch?v=r6JK-gRELI0) 0:00.1–0:01.4 |
| No No No | w | *Obsession* (2026), "Nice Date" clip | [YouTube](https://www.youtube.com/watch?v=MeHvxJGtz88) 0:53.0–0:59.1 |
| Are You Sure? | e | *Invincible*, Omni-Man | [YouTube](https://www.youtube.com/watch?v=-QT1ek1TPIQ&t=324) 5:24.9–5:26.0 |
| Woo I'm Bouta Make a Name for Myself | r | *Deadpool & Wolverine*, Gambit | [YouTube](https://www.youtube.com/watch?v=vlle7qJUg9g) 0:02.9–0:05.1 |
| Why Are You the Way That You Are? | t | *The Office*, Michael Scott | [YouTube](https://www.youtube.com/watch?v=aYmOqPFyJPw) 0:03.0–0:04.4 |
| No God Please No | y | *The Office*, "Toby Returns" | [YouTube](https://www.youtube.com/watch?v=CQ_eDE0OMds&t=104) 1:44.0–1:57.0 |
| Yeah, Science! | u | *Breaking Bad*, Jesse Pinkman | [YouTube](https://www.youtube.com/watch?v=saYqNH0OjbY&t=29) 0:29.8–0:31.1 |
| Say My Name | i | *Breaking Bad*, Walter White | [YouTube](https://www.youtube.com/watch?v=MPYlxeG-8_w&t=131) 2:11.5–2:12.5 |
| KASAA! | o | *Hollow Knight*, Quirrel's combat shout from the Uumuu fight | [YouTube](https://www.youtube.com/watch?v=pfpj8FPGozY&t=32) 0:32.2–0:33.0 |
| Bacanada | p | *Hollow Knight*, Iselda in Dirtmouth | [YouTube](https://www.youtube.com/watch?v=ekz4-SNVJjU) 0:00.5–0:02.6 |
| Trobbio! | a | *Hollow Knight: Silksong*, Trobbio | [YouTube](https://www.youtube.com/watch?v=u7ow7Oz5NN0&t=17) 0:17.7–0:19.2 |
| Trick 21:21 Scream | s | Grief stream 1 | [YouTube](https://www.youtube.com/watch?v=rDeYgmWMYJ8&t=1286) 21:27.0–21:35.5 |
| Trick 30:23 Scream | d | Grief stream 1 | [YouTube](https://www.youtube.com/watch?v=rDeYgmWMYJ8&t=1823) 30:23.2–30:24.9 |
| Stressless | f | Provided clip | |
| Mmkoydokoy | g | Provided clip | |
| Do Magnets | h | Provided clip | |
| Who Violently Murdered Thad? | j | Provided clip | 0:29.2–0:32.6 of the source video |
