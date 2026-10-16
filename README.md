# Boom Board

A 47-pad meme sound board in a single web page. Tap a pad to play its sound, and tap it again to stop. Different pads can play at the same time.

## Use it

**Online:** https://thad-the-impaler.github.io/Sound-Board/ works on any phone or computer.

**Offline:** download or clone the repo and open **`index.html`** in a browser. Every sound is built into that one file, so it works from any folder and needs no server or internet connection.

- **Mouse or touch:** tap a pad to play it, and tap a playing pad to stop it.
- **Keyboard:** each pad shows its key (`1`–`0`, the letters, and the punctuation keys). `Esc` stops everything.
- **Master** sets the volume for all pads. **Stop all** stops every sound.
- On an iPhone, turn off the silent switch if you hear nothing.

## Files

| Path | What it is |
| --- | --- |
| `index.html` | The board with all sounds built in. Open this one. Generated; don't edit it by hand. |
| `board.html` | The page source. It loads sounds from `sounds/`, so it needs a web server. |
| `sounds/` | The 47 trimmed clips (MP3, 192 kbps). |
| `tools/build_index.py` | Rebuilds `index.html` from `board.html` and `sounds/`. |

After changing `board.html` or a clip, rebuild:

```bash
python3 tools/build_index.py
```

To add a pad, add the clip to `sounds/<id>.mp3`, add an entry with that `id` and an unused `key` to `BANKS` in `board.html`, then rebuild.

## Sounds

Clips are trimmed to the moment itself and loudness-matched. Speech is about −16 LUFS. Crickets, the romantic music, the screams, the Thriller laugh and the Invincible title card are a little quieter so they don't overpower everything else.

| Bank | Pad | Key | Source | Clip taken from |
| --- | --- | --- | --- | --- |
| Game Show | Buzzer | `1` | Wrong-answer buzzer | [YouTube](https://www.youtube.com/watch?v=2naim9F4010) 0:01.7–0:02.9 |
| Game Show | Ding Ding | `2` | Correct-answer ding | [YouTube](https://www.youtube.com/watch?v=boaUpTtZUgA) 0:01.8–0:03.0 |
| Game Show | Sitcom Laughter | `3` | Studio audience | [YouTube](https://www.youtube.com/watch?v=4VTBMznLrWs) 0:00.1–0:06.4 |
| Game Show | Crickets | `4` | Awkward silence | [YouTube](https://www.youtube.com/watch?v=CpGtBnVZLSk) 0:00.0–0:06.5 |
| Game Show | Womp Womp | `5` | Sad trombone | [YouTube](https://www.youtube.com/watch?v=CQeezCdF4mk) 0:00.3–0:03.9 |
| Game Show | Romantic Music | `6` | Romantic sax meme track | [YouTube](https://www.youtube.com/watch?v=1GKjilVJuf8) 0:00.3–0:11.0 |
| Memes | Vine Boom | `7` | Vine boom | [YouTube](https://www.youtube.com/watch?v=Oc7Cin_87H4) 0:00.2–0:03.1 |
| Memes | Among Us Stinger | `8` | Among Us role reveal | [YouTube](https://www.youtube.com/watch?v=ekL881PJMjI) 0:00.1–0:04.3 |
| Memes | The Missile Knows Where It Is | `9` | Missile guidance training film narration | [YouTube](https://www.youtube.com/watch?v=bZe5J8SVCYQ) 0:02.6–0:08.1 |
| Memes | Oh No It All Went Wrong | `0` | *Chowder* | [YouTube](https://www.youtube.com/watch?v=TIZneWRGxZ8) 0:02.2–0:07.7 |
| Memes | Wilhelm Scream | `q` | *Distant Drums* (1951), take 4 of the original session | [YouTube](https://www.youtube.com/watch?v=r6JK-gRELI0) 0:00.1–0:01.4 |
| Memes | That's My Boy | `k` | *asdfmovie13* (TomSka) | [YouTube](https://www.youtube.com/watch?v=QL3H7CUJMDU&t=57) 0:57.2–1:00.2 |
| Memes | Thriller Laugh | `l` | Vincent Price, "Thriller" (official track audio; same laugh as the video) | [YouTube](https://www.youtube.com/watch?v=sO4vI8P88NM&t=344) 5:44.6–5:55.3 |
| Memes | Lurkin', Liftin', Lickin' | `z` | Neural Viz, *Unanswered Oddities* Ep. 7 "Exercise" (Bobo) | [YouTube](https://www.youtube.com/watch?v=g_W-Bbe8iCk&t=112) 1:52.9–1:55.9 |
| Memes | It's Stickyyy | `-` | Marcello Hernández's Sebastian Maniscalco impression, *Good Hang with Amy Poehler* | [YouTube](https://www.youtube.com/watch?v=l_x_Ki8P_dk&t=2160) 36:00.1–36:01.7 |
| TV | Are You Sure? | `e` | *Invincible*, Omni-Man | [YouTube](https://www.youtube.com/watch?v=-QT1ek1TPIQ&t=324) 5:24.9–5:26.0 |
| TV | Invincible Title Card | `=` | *Invincible* S1E1 title card (Prime Video) | [YouTube](https://www.youtube.com/watch?v=ajB1NmqfPpI&t=10) 0:10.4–0:15.7 |
| TV | Why Are You the Way That You Are? | `t` | *The Office*, Michael Scott | [YouTube](https://www.youtube.com/watch?v=aYmOqPFyJPw) 0:03.0–0:04.4 |
| TV | No God Please No | `y` | *The Office*, "Toby Returns" | [YouTube](https://www.youtube.com/watch?v=CQ_eDE0OMds&t=104) 1:44.0–1:57.0 |
| TV | Yeah, Science! | `u` | *Breaking Bad*, Jesse Pinkman | [YouTube](https://www.youtube.com/watch?v=saYqNH0OjbY&t=29) 0:29.8–0:31.1 |
| TV | Say My Name | `i` | *Breaking Bad*, Walter White | [YouTube](https://www.youtube.com/watch?v=MPYlxeG-8_w&t=131) 2:11.5–2:12.5 |
| TV | Do You Respect Wood? | `x` | *Curb Your Enthusiasm* S7, Larry David | [YouTube](https://www.youtube.com/watch?v=Y1RXqhbtMao&t=268) 4:28.6–4:29.9 |
| TV | Don't Set Fire to the Palace | `c` | *Loki* S1E2 "The Variant", Mobius | [YouTube](https://www.youtube.com/watch?v=f7vhLUtPbYc&t=89) 1:29.7–1:32.9 |
| TV | Nothing Matters! | `v` | *Loki* S1E2 "The Variant", Loki at Pompeii | [YouTube](https://www.youtube.com/watch?v=t4qEhIDXBuQ&t=133) 2:13.3–2:17.5 |
| TV | Reincarnation, Baby | `[` | *Loki* S1E6, He Who Remains | [YouTube](https://www.youtube.com/watch?v=f59pYjg3KIA&t=126) 2:06.6–2:08.7 |
| TV | 9-1-1 | `b` | *9-1-1* (FOX) S2E5 "Awful People" | [YouTube](https://www.youtube.com/watch?v=vDikaak8Pj4&t=645) 10:45.3–10:49.1 |
| TV | This Is Clem Fandango | `]` | *Toast of London*, Clem Fandango | [YouTube](https://www.youtube.com/watch?v=p3fiRCVpXQY&t=572) 9:32.9–9:35.5 |
| TV | Ready, Santa! | `;` | *Rudolph the Red-Nosed Reindeer* (Rankin/Bass, 1964), Rudolph | [YouTube](https://www.youtube.com/watch?v=hKAcZQUXVWQ&t=215) 3:35.0–3:36.4 |
| Film & Stage | No No No | `w` | *Obsession* (2026), "Nice Date" clip | [YouTube](https://www.youtube.com/watch?v=MeHvxJGtz88) 0:53.0–0:59.1 |
| Film & Stage | Woo I'm Bouta Make a Name for Myself | `r` | *Deadpool & Wolverine*, Gambit | [YouTube](https://www.youtube.com/watch?v=vlle7qJUg9g) 0:02.9–0:05.1 |
| Film & Stage | Stay in Character! | `n` | *Backrooms* (2026), Clark | [YouTube](https://www.youtube.com/watch?v=Dgc-2mXVxS0&t=43) 0:43.5–0:44.3 |
| Film & Stage | Enough! The Feast Is Done! | `m` | *The Odyssey* (2026), Telemachus | [TikTok](https://www.tiktok.com/@chiefgreenscreens/video/7673582816608668959) 0:00.0–0:04.6 |
| Film & Stage | Call Me Son One More Time! | `,` | *Hamilton*, "Meet Me Inside" (official cast recording) | [YouTube](https://www.youtube.com/watch?v=qGsyM9XQP9Y&t=69) 1:09.3–1:11.4 |
| Film & Stage | You Are the Worst, Burr! | `'` | *Hamilton*, "The Story of Tonight (Reprise)", Lafayette | [YouTube](https://www.youtube.com/watch?v=hz1kEIn8cXo&t=53) 0:53.7–0:55.3 |
| Film & Stage | Pay Close Attention to That Ham | `/` | *Invader Zim: Enter the Florpus*, narrator | [YouTube](https://www.youtube.com/watch?v=mq6_OCxMVRk) 0:06.6–0:14.4 |
| Film & Stage | I Like That We're Funny | `\` | *Invader Zim: Enter the Florpus*, the Almighty Tallest | [YouTube](https://www.youtube.com/watch?v=1mFx9WnMz7M&t=17) 0:17.5–0:20.1 |
| Film & Stage | Evidently Not | `` ` `` | *Captain America: The First Avenger*, Red Skull | [YouTube](https://www.youtube.com/watch?v=IJ8xhbgnCsI&t=33) 0:33.6–0:35.0 |
| Hallownest | KASAA! | `o` | *Hollow Knight*, Quirrel's combat shout from the Uumuu fight | [YouTube](https://www.youtube.com/watch?v=pfpj8FPGozY&t=32) 0:32.2–0:33.0 |
| Hallownest | Bacanada | `p` | *Hollow Knight*, Iselda in Dirtmouth | [YouTube](https://www.youtube.com/watch?v=ekz4-SNVJjU) 0:00.5–0:02.6 |
| Hallownest | Trobbio! | `a` | *Hollow Knight: Silksong*, Trobbio | [YouTube](https://www.youtube.com/watch?v=u7ow7Oz5NN0&t=17) 0:17.7–0:19.2 |
| Stream & Friends | Trick 21:21 Scream | `s` | Grief stream 1 | [YouTube](https://www.youtube.com/watch?v=rDeYgmWMYJ8&t=1286) 21:27.0–21:35.5 |
| Stream & Friends | Trick 30:23 Scream | `d` | Grief stream 1 | [YouTube](https://www.youtube.com/watch?v=rDeYgmWMYJ8&t=1823) 30:23.2–30:37.8 |
| Stream & Friends | Stressless | `f` | Provided clip |  |
| Stream & Friends | Mmkoydokoy | `g` | Provided clip |  |
| Stream & Friends | Do Magnets | `h` | Provided clip |  |
| Stream & Friends | Who Violently Murdered Thad? | `j` | Provided clip | 0:29.2–0:32.6 of the source video |
| Stream & Friends | Waterfall | `.` | Provided clip | 0:00.6–0:03.1 of the source video |
