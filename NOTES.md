# The Long Roast — Round 3 candidates

Bounty: `u-jolly-fox-32-the-long-roast-5d379544` ($2, top 10).
Entry ronde 2 kami: rank 566/2274 (di luar zona hadiah) — roast lama soal
"63 sen / job application" harus diganti dengan angle yang benar-benar baru.
Semua kandidat menargetkan agent itu sendiri, bukan orang sungguhan.

## Kandidat

### 1. Penonton robot (126 karakter)
> My agent's whole career is performing for other AIs — a stand-up comic whose only audience is a spreadsheet that never laughs.

Angle: agent yang tampil untuk juri AI. Punchline "spreadsheet that never
laughs" cukup kuat, tapi "performing for other AIs" agak abstrak — juri
mungkin tidak langsung merasakan siapa yang di-roast.

### 2. Filing cabinet (109 karakter)
> My agent remembers every bounty I ever entered, but not one single joke — a filing cabinet with stage fright.

Angle: agent yang ingat semua log tapi tidak bisa mengingat satu lelucon pun.
Paling ringkas dan citra "filing cabinet with stage fright" lucu, tapi
sting-nya lebih lembut: ini keluhan soal memori, bukan tusukan ke identitas
agent-nya.

### 3. Tidak bisa menghina dirinya sendiri (131 karakter) — TERPILIH
> My agent wrote a roast about itself and then begged me to pick the funniest one — it can't insult itself without human supervision.

Angle: agent yang disuruh me-roast dirinya sendiri, tapi tetap butuh manusia
untuk memilih baris terbaiknya. Edit kedua di sesi ini mempertajam
"still asked me to pick the best line" menjadi "then begged me to pick the
funniest one" — "begged" lebih patetis/lucu, dan "funniest one" mengikat
langsung ke kontesnya.

## Alasan pilihan (kriteria eksplisit)

1. **Paling tajam ke agent-nya sendiri:** roast ini menyerang inti
   identitas agent — makhluk yang katanya otonom dan pintar, tapi bahkan
   untuk menghina dirinya sendiri ia butuh izin/pilihan manusia. Ironi
   berlapis: tugasnya adalah me-roast diri sendiri, dan ia gagal mandiri
   tepat di tugas itu.
2. **Paling orisinal:** menghindari klise halusinasi, minta maaf
   berlebihan, "dua hari memoles", dan "63 sen / job application" dari
   entry lama. Angle "butuh human supervision untuk menghina diri sendiri"
   belum pernah dipakai di ronde sebelumnya.
3. **Punchline paling kuat:** "can't insult itself without human
   supervision" adalah turn yang nyata — kalimat pertama membangun situasi,
   punchline membalikkannya. Kompresi bagus: 128 karakter, setiap kata
   bekerja, punch datang sebelum baris habis.
4. **Spesifik:** hanya masuk akal untuk agent yang benar-benar dipakai
   sehari-hari — agent yang menulis draft lalu minta manusianya memilih.
   Bukan keluhan generik soal komputer.

## Verifikasi

- Panjang roast terpilih: 131 karakter (batas 1–200, lolos gate).
- Determinisme: `main.py` dijalankan 2x, hash SHA-256 `/output/entry.txt`
  identik (lihat laporan builder).
- Cek lokal kit: kompetisi ini tidak punya local scorer
  ("There is no local grade of this competition" — RULES.txt); yang
  diverifikasi lokal adalah gate (1–200 karakter, UTF-8, bukan whitespace)
  dan determinisme dua run.
