# 🏓 Pong – Tkinter

Egy egyszerű, retro stílusú Pong játék Pythonban, **Tkinter** grafikus felülettel.

A játék célja, hogy az alsó ütő segítségével minél tovább pattintsd vissza a leeső labdát. Minden sikeres visszapattanásért pontot kapsz, a labda leesésekor pedig életedből veszítesz.

---

## 🎮 Játék indítása

1. Telepítsd a [Python](https://www.python.org/) (ajánlott: **3.10 vagy újabb**)
2. Klónozd vagy töltsd le a repót.
3. Navigálj a mappába, majd futtasd a játékot:

```bash
python gui.py


⌨️ Irányítás
⬅️ Balra mozgás: Left nyíl

➡️ Jobbra mozgás: Right nyíl

⏯️ Indítás / Szünet: Space

🧠 Játékszabályok
A játék alapértelmezetten szünetel, nyomj Space-t az indításhoz.

A piros négyzet a labda, a fekete téglalapok pedig az ütő.

Ha a labda eltalálja a pálya alját, veszítesz egy életet.

Ha minden életed elfogy, megjelenik egy "Game Over" ablak.

A labda pattog a falakról, az ütőről, valamint pontot szerezhetsz extra szögekkel való eltalálásért is.

🗂️ Fájlok
Fájlnév	Leírás
gui.py	Tkinter alapú grafikus felület és fő ciklus
pong.py	A játék logikája (ütő, labda, pálya, pontszám)
requirements.txt	Függőségek (jelenleg üres)
.gitignore	Git által kizárt fájlok listája
screenshot.png	Képernyőkép a játékról
README.md	Ez a fájl

🖼️ Képernyőkép
A játék futás közben így néz ki:
![alt text](image.png)

A fenti kép a játék indulási állapotát mutatja, ahol a piros négyzet a labda, a fekete téglalapok pedig az ütő.

📝 Licenc
Ez a projekt nyílt forráskódú. Terjeszthető, másolható, módosítható az MIT licenc feltételei szerint.

👨‍💻 Szerző
Készült saját tanulási és szórakozási célból.
Ha szeretnél hozzájárulni vagy ötleted van, nyugodtan nyiss issue-t vagy pull request-et!