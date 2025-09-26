# Roguelike Game - review project

This is an extended exercise offered as supplementary review material for `SDEV1001 - Programming Fundamentals`.

You'll be retracing the concepts we've learned so far to create a text-based roguelike RPG.
(Hey, at least I didn't say "early access open world MMO with crafting and a battle pass").

---

- If you just want to follow along, clone this repo (if you haven't already) and proceed through the README.

- If you want to work on the game interactively, [fork this repository](https://docs.github.com/assets/cb-34352/mw-1440/images/help/repository/fork-button.webp) and clone it so you can make changes.

It's meant to be followed from the beginning, but you can jump in at whatever module you want. 

It is recommended to make your terminal full-height and full-width when running the program.

---

Developing the game is *part of* the game -- enjoy!

---

Click on any **Chapter 0x: Title** to expand or collapse its text.

<br />
<details>
  <summary><b>Chapter 01: <u>Introduction</u></b></summary>
  <br />
  <p>    Hark, adventurer! 
  
  Your name is N̴̲̈́ä̶͗̀͆̀ͅm̷̻͎͆͊̊́ȩ̷̠̟̪̟͎̦͎̮̾̓́E̴̤̮̙̥̫̤̻̍̌̉͆͑̽̽͘͜r̷̡͙̯͚̠̬͚̈̓̽̄̚r̵̻̅̏͝͠o̶̠̩̹̎͆̒́͗́̎r̵̨͛͌̉́̄̀͛:  ̶͕͍̇̿̕n̵̨̫̉̿͌̊a̶̡͕̙̎̂͆̌m̴̨͖̫̐̏e̴̛̙̼͖͊͌ͅ ̸͖̳̪͆'̴̺̙͙͇̌̀͗h̸̜͂e̴̢̙͍̫̐̄r̵͉̰̎́o̸̞͎̽_̸͍̱̳̉͜ṇ̷̄͝ą̸̥̳͎̒͌m̴̺̞͆e̴͇͕͍͐̿̏'̶̼̒̽͐̐ ̸̰̒͠i̶̡̮̘͔͒s̴̜̒ ̷̬͈̣̲̏̎̈ń̸͉͇̣̐̑͠o̵͎̼͙͛t̷̩̆͊̏ ̷̩̳̈͘͝d̴̤͝e̸͈̝̱̎f̴͓̹̮̞́̎̍̃ĭ̴̧͕̗̅̔n̸̡̬͐̈̀e̶̖͛͒ͅḋ̴̛̻̀͘,  and you are an apprentice born and raised here, in the burgeoning lands of Nait.

  You currently have but one aspiration: to master the art of **snakecharming**, and use it to earn great wealth & renown. You'd also settle for, you know, stable living conditions, a home of your own, and enough personal time to spend around your hobbies & loved ones, but who's counting.

  Right now, you're still a complete novice, but that doesn't dampen your ambition & imagination.
  Every night, snakes flood your dreams: pythons, asps, Komodo spitting cobras.
  Well... they did, before you were imprisoned, anyway.

  Oh, yeah. Forgot to mention that.
    
  See, about a month ago, you entered the service of your liege, Count Essdev -- lord of the rich, sun-filled lands south of Feltham.
  
  As it happens, Count Essdev recently developed a penchant for snakes. When you caught wind of this, you presented yourself to him as a master snakecharmer, ready to entertain the royal court -- for ample pay, of course.
  
  The Count believed the lie.

  Predictably, when it came time to demonstrate your skills to the court, you panicked. All you could think of were all the worst things the Count might do once he found out you lied. You hatched a plan that only a fearful mind would consider a bright idea: You'd disguise your pet Cat GePetto as a snake, in hopes that its lithe feline movements could fool the Count and his courtiers.
  

  Count Essdev immediately saw through the ruse, becoming inconsolably furious. He ordered you to be thrown in the deepest, most dangerous parts of his labyrinthine dungeons forever.

  So begins your quest to break free.
    
  > (Proceed to Chapter 02.)
  
  </p> 

</details>

<br />

<details>
  <summary><b>Chapter 02: <u>Version Control</u></b></summary>
  <br />
  <p>
   Wakey-wakey! It's another lovely day in the oubliette.

   Your jailer, a moustached man with a wiry silhouette, drops your daily meal -- a slice of stale bread -- down the chute. Only, it lands on the floor of your cell with a... metallic clang!? Even the stalest bread wouldn't make that sound.
   
   You reach for it curiously, and your fingers curl around a scroll, wrapped around a fork. The scroll casts a dim light as you unfurl it. It simply says `README`, but then the words shift and morph.

   `Wanna get out of here?`, it now reads. *Obviously*, you mutter to yourself.

   The calligraphy swirls around again.

   `I can get you out of here, there, and everywhere, baby.`

   `Back to the year 6̸̰̟͕͛͘͜͠c̵͉̞̟̈́̉9̸͓̻̳͔̈́͠2̵̜͝ȧ̴̤͑̓̚f̸͇͉̱̚7̵͎̪̾͝, even. Back to the beginning.`

   `You just gotta say the words.`

   *What words*? 

   The ink on the scroll transforms again:

   `git checkout 6c92af7` 
  
  You've heard of incantations like this before -- foul, heretical magic from the extraplanar realm of Git!

  `Just hurry up and recite the spell. Then run the program.` the scroll's words urge hastily.

  *Run? Run where? A program for what?*
  
  `Listen, you ask too many questions. I'm just a piece of paper.`

  `And just so ya know, there's a price on that spell.`

  `It'll decapitate ya.`
  
  *What? [My HEAD](https://blog.git-init.com/what-is-head-in-git/)? Seriously?*

  `Yup. It'll pull your HEAD clean off.`

  `That's the kinda price of usin' Git magic willy-nilly.`

  `You'll be fine though. Totally reversible. Done this a lot.`

  *Wh.. I... guess it's my only chance...*

  `Just don't cast that spell anywhere near me.`

  `I don't want no detached HEAD bleedin' all over my precious magic ink.` 

  `Oh, and grab that fork if you want. Might come in handy.`

  <br />

  > 1. Fork this repository and continue working from there if you want to make your own changes to the game. If you only want to observe, just keep following the `README`.
  
  > 2. Run the following terminal command inside this repo to visit the project state at an earlier commit (in this case, the commit `6c92af7`):
  >   `git checkout 6c92af7`

  > 3. Then, open `roguelike.py` and run the program.

  > 4. Proceed to Chapter 03.

  </p> 
</details>
