# -*- coding: utf-8 -*-
"""Individual offer pages under a concierge service (yacht classes and experiences).

Key = "<service slug>/<offer anchor>". Each offer becomes its own page at
services/<service slug>/<offer anchor>.html.

"img" is (folder under assets/img, file name without extension).
"see" lists related pages shown as links at the bottom.
Edit text here, then run `python _build/build.py`.
"""
from content_dest import L

POINTS_TITLE = L("What to expect", "Yang bisa Anda harapkan")
SEE_TITLE = L("You may also like", "Anda mungkin juga suka")

OFFERS = {
    # ------------------------------------------------------------------ Yacht
    "yacht-boat-phinisi/vvip": {
        "img": ("services/yacht-boat-phinisi", "vvip"),
        "lead": L("Our most exclusive way to see Komodo: a flagship phinisi, entirely yours.",
                  "Cara paling eksklusif menikmati Komodo: phinisi terbaik, sepenuhnya untuk Anda."),
        "paras": [
            L("VVIP charters are for guests who want the very best vessel available: spacious suites, generous decks and lounges, and a crew and chef dedicated to your group alone.",
              "Charter VVIP ditujukan bagi tamu yang menginginkan kapal terbaik yang tersedia: kabin suite yang luas, dek dan lounge yang lapang, serta kru dan chef yang khusus melayani rombongan Anda."),
            L("Every part of the voyage is planned around you, from the route and the pace of each day to the menu and the moments you want to celebrate.",
              "Setiap bagian perjalanan dirancang sesuai keinginan Anda, mulai dari rute dan ritme setiap hari hingga menu dan momen yang ingin Anda rayakan."),
        ],
        "points": [
            L("Private charter of a top-tier phinisi", "Charter pribadi phinisi kelas teratas"),
            L("Spacious suite cabins and open decks", "Kabin suite yang luas dan dek terbuka"),
            L("Dedicated crew, tour guide and chef", "Kru, pemandu wisata, dan chef khusus"),
            L("A route and daily schedule designed around you", "Rute dan jadwal harian yang dirancang untuk Anda"),
            L("Meals, snorkeling equipment and Labuan Bajo transfers arranged", "Makanan, peralatan snorkeling, dan transfer di Labuan Bajo sudah diatur"),
        ],
        "see": ["packages/private-trip.html", "packages/honeymoon.html", "packages/4d3n.html"],
    },
    "yacht-boat-phinisi/vip": {
        "img": ("services", "yacht-boat-phinisi"),
        "lead": L("Elegant phinisi with private cabins and attentive service.",
                  "Phinisi elegan dengan kabin pribadi dan pelayanan yang penuh perhatian."),
        "paras": [
            L("VIP boats combine the charm of a traditional phinisi with the comfort of a boutique stay: well-appointed private cabins, shaded decks and a crew that looks after the details.",
              "Kapal VIP memadukan pesona phinisi tradisional dengan kenyamanan penginapan butik: kabin pribadi yang tertata apik, dek yang teduh, dan kru yang memperhatikan setiap detail."),
            L("It is a popular choice for families and small groups who want a private or semi-private trip with a high level of comfort.",
              "Pilihan favorit bagi keluarga dan rombongan kecil yang menginginkan trip private atau semi-private dengan tingkat kenyamanan tinggi."),
        ],
        "points": [
            L("Well-appointed private cabins", "Kabin pribadi yang tertata apik"),
            L("Comfortable decks for relaxing between islands", "Dek yang nyaman untuk bersantai di antara pulau"),
            L("Experienced crew and tour guide", "Kru dan pemandu wisata berpengalaman"),
            L("Meals on board, mineral water, coffee and tea", "Makan di kapal, air mineral, kopi, dan teh"),
            L("Snorkeling equipment and life jackets", "Peralatan snorkeling dan jaket pelampung"),
        ],
        "see": ["packages/private-trip.html", "packages/3d2n.html", "packages/anniversary.html"],
    },
    "yacht-boat-phinisi/deluxe": {
        "img": ("packages", "private-trip"),
        "lead": L("Comfortable boats with private cabins, and very good value.",
                  "Kapal yang nyaman dengan kabin pribadi, dengan harga yang sangat sepadan."),
        "paras": [
            L("Deluxe boats are a relaxed way to explore the park over one or more nights. You get your own cabin, good food and an experienced crew, without paying for extras you do not need.",
              "Kapal Deluxe adalah cara santai untuk menjelajahi taman nasional selama satu malam atau lebih. Anda mendapatkan kabin sendiri, makanan yang lezat, dan kru berpengalaman, tanpa membayar fasilitas tambahan yang tidak Anda perlukan."),
            L("They suit couples, friends and travellers joining a sharing trip who still want privacy at the end of the day.",
              "Cocok untuk pasangan, teman, dan wisatawan yang mengikuti sharing trip namun tetap menginginkan privasi di penghujung hari."),
        ],
        "points": [
            L("Private cabin on a comfortable boat", "Kabin pribadi di kapal yang nyaman"),
            L("Available for private charter or sharing trips", "Tersedia untuk charter pribadi maupun sharing trip"),
            L("Meals on board, mineral water, coffee and tea", "Makan di kapal, air mineral, kopi, dan teh"),
            L("Tour guide, snorkeling equipment and life jackets", "Pemandu wisata, peralatan snorkeling, dan jaket pelampung"),
        ],
        "see": ["packages/sharing-trip.html", "packages/3d2n.html", "packages/private-trip.html"],
    },
    "yacht-boat-phinisi/speedboat": {
        "img": ("packages", "one-day-trip"),
        "lead": L("The fastest way to see the highlights of Komodo National Park.",
                  "Cara tercepat untuk menikmati destinasi utama Taman Nasional Komodo."),
        "paras": [
            L("A speedboat covers in one day what a larger boat reaches in two. It is ideal for day trips, tight schedules and early starts to reach Padar before the crowds.",
              "Speedboat dapat menjangkau dalam satu hari apa yang ditempuh kapal besar dalam dua hari. Cocok untuk trip sehari, jadwal yang padat, dan berangkat pagi agar tiba di Padar sebelum ramai."),
            L("Choose a private speedboat for your own group and timing, or join a sharing trip on a fixed route.",
              "Pilih speedboat private untuk rombongan dan jadwal Anda sendiri, atau bergabung dalam sharing trip dengan rute yang sudah ditentukan."),
        ],
        "points": [
            L("Full-day trips, private or sharing", "Trip sehari penuh, private atau sharing"),
            L("Early departure for Padar, Pink Beach and Komodo Island", "Berangkat pagi menuju Padar, Pink Beach, dan Pulau Komodo"),
            L("Snorkeling stops at Taka Makassar and Manta Point", "Singgah untuk snorkeling di Taka Makassar dan Manta Point"),
            L("Tour guide, snorkeling equipment and life jackets", "Pemandu wisata, peralatan snorkeling, dan jaket pelampung"),
        ],
        "see": ["packages/one-day-trip.html", "destinations/padar-island.html", "destinations/manta-point.html"],
    },
    # ------------------------------------------------------------ Experiences
    "experiences/island-hopping": {
        "img": ("destinations", "kelor-island"),
        "lead": L("Padar, Komodo, Pink Beach and the quieter islands in between.",
                  "Padar, Komodo, Pink Beach, dan pulau-pulau yang lebih tenang di antaranya."),
        "paras": [
            L("Island hopping is the heart of any Komodo trip. Each island is different: a summit view at Padar, dragons on Komodo and Rinca, pink sand, sandbanks and small islands with empty beaches.",
              "Island hopping adalah inti dari setiap perjalanan ke Komodo. Setiap pulau menawarkan hal berbeda: pemandangan dari puncak Padar, komodo di Pulau Komodo dan Rinca, pasir merah muda, gosong pasir, dan pulau-pulau kecil dengan pantai yang sepi."),
            L("We plan the order of the islands around tides, light and visitor numbers, so you reach the famous places at the best time of day.",
              "Kami mengatur urutan pulau berdasarkan pasang surut, cahaya, dan jumlah pengunjung, sehingga Anda tiba di tempat-tempat terkenal pada waktu terbaik."),
        ],
        "points": [
            L("A route built around what you most want to see", "Rute yang disusun berdasarkan apa yang paling ingin Anda lihat"),
            L("By speedboat in a day, or by phinisi over several days", "Dengan speedboat dalam sehari, atau dengan phinisi selama beberapa hari"),
            L("Ranger-guided walks to see Komodo dragons", "Trekking bersama ranger untuk melihat komodo"),
            L("Time to swim and snorkel between islands", "Waktu untuk berenang dan snorkeling di antara pulau"),
        ],
        "see": ["destinations/padar-island.html", "destinations/komodo-island.html", "destinations/pink-beach.html", "destinations/kelor-island.html"],
    },
    "experiences/snorkeling": {
        "img": ("services", "experiences"),
        "lead": L("Manta rays, turtles and coral gardens, a few metres below the surface.",
                  "Pari manta, penyu, dan taman karang, hanya beberapa meter di bawah permukaan."),
        "paras": [
            L("Komodo has some of the richest reefs in Indonesia, and many of the best sights can be enjoyed with just a mask and fins.",
              "Komodo memiliki terumbu karang terkaya di Indonesia, dan banyak keindahannya bisa dinikmati hanya dengan masker dan fin."),
            L("We choose sites to match your confidence in the water, from calm bays for beginners to drift snorkeling with manta rays, always with a guide who knows the currents.",
              "Kami memilih lokasi sesuai kenyamanan Anda di air, dari teluk yang tenang untuk pemula hingga drift snorkeling bersama pari manta, selalu didampingi pemandu yang memahami arus."),
        ],
        "points": [
            L("Sites chosen for your experience level", "Lokasi yang dipilih sesuai tingkat pengalaman Anda"),
            L("Guide in the water with you", "Pemandu mendampingi Anda di air"),
            L("Snorkeling equipment and life jackets provided", "Peralatan snorkeling dan jaket pelampung disediakan"),
            L("Timing planned around tides and currents", "Waktu yang diatur sesuai pasang surut dan arus"),
        ],
        "see": ["destinations/manta-point.html", "destinations/siaba-island.html", "destinations/manjarite-island.html", "destinations/kanawa-island.html"],
    },
    "experiences/diving": {
        "img": ("destinations", "batu-bolong"),
        "lead": L("World-class diving, from gentle reefs to thrilling current dives.",
                  "Penyelaman kelas dunia, dari terumbu yang tenang hingga titik selam berarus yang menantang."),
        "paras": [
            L("Strong currents bring life to Komodo's reefs: dense schools of fish, turtles, reef sharks and manta rays. It is one of the most exciting places in the world to dive.",
              "Arus yang kuat menghidupkan terumbu karang Komodo: kawanan ikan yang padat, penyu, hiu karang, dan pari manta. Ini adalah salah satu tempat menyelam paling menarik di dunia."),
            L("We arrange dives and courses with established dive centres, matched to your certification and experience, and combine them with the rest of your trip.",
              "Kami mengatur penyelaman dan kursus bersama pusat selam terpercaya, disesuaikan dengan sertifikasi dan pengalaman Anda, serta memadukannya dengan seluruh perjalanan Anda."),
        ],
        "points": [
            L("Fun dives for certified divers", "Fun dive untuk penyelam bersertifikat"),
            L("Introductory dives and courses for beginners", "Penyelaman perkenalan dan kursus untuk pemula"),
            L("Established dive centres and experienced guides", "Pusat selam terpercaya dan pemandu berpengalaman"),
            L("Leisure, diving or combination trips", "Trip santai, diving, atau kombinasi keduanya"),
        ],
        "see": ["destinations/batu-bolong.html", "destinations/manta-point.html", "packages/4d3n.html"],
    },
    "experiences/water-activities": {
        "img": ("services/experiences", "water-activities"),
        "lead": L("Kayaks, paddleboards and long swims in calm, clear water.",
                  "Kayak, paddleboard, dan berenang santai di air yang tenang dan jernih."),
        "paras": [
            L("Between the bigger sights, Komodo's sheltered bays are perfect for slowing down. Paddle along a quiet shoreline, float over a reef or simply swim from the boat.",
              "Di sela kunjungan ke tempat-tempat utama, teluk-teluk terlindung di Komodo sangat pas untuk bersantai. Mendayung di sepanjang pantai yang sepi, mengapung di atas terumbu, atau sekadar berenang dari kapal."),
            L("Tell us what you enjoy and we will make sure the right equipment is on board and the stops are chosen for calm water.",
              "Ceritakan apa yang Anda sukai, dan kami akan memastikan peralatan yang tepat tersedia di kapal serta memilih tempat singgah dengan air yang tenang."),
        ],
        "points": [
            L("Kayaking and paddleboarding in sheltered bays", "Kayak dan paddleboard di teluk yang terlindung"),
            L("Swimming stops at quiet beaches and sandbanks", "Singgah untuk berenang di pantai dan gosong pasir yang sepi"),
            L("Equipment arranged in advance for your boat", "Peralatan diatur sebelumnya untuk kapal Anda"),
            L("Suitable for families and all ages", "Cocok untuk keluarga dan segala usia"),
        ],
        "see": ["destinations/taka-makassar.html", "destinations/sebayur-island.html", "destinations/kanawa-island.html"],
    },
    "experiences/honeymoon": {
        "img": ("packages", "honeymoon"),
        "lead": L("A private journey for two, with every detail taken care of.",
                  "Perjalanan pribadi untuk berdua, dengan setiap detail yang sudah diurus."),
        "paras": [
            L("A yacht to yourselves, sunrise on Padar, quiet beaches and dinner on deck as the sun goes down. Komodo is a wonderful place to begin a marriage.",
              "Yacht hanya untuk Anda berdua, matahari terbit di Padar, pantai yang tenang, dan makan malam di dek saat matahari terbenam. Komodo adalah tempat yang indah untuk memulai pernikahan."),
            L("We plan the trip around the two of you, including the small touches: a decorated cabin, a special dinner, or a photographer for a morning.",
              "Kami merencanakan perjalanan khusus untuk Anda berdua, termasuk sentuhan kecilnya: kabin yang dihias, makan malam istimewa, atau fotografer untuk satu pagi."),
        ],
        "points": [
            L("Private yacht with a cabin prepared for two", "Yacht pribadi dengan kabin yang disiapkan untuk berdua"),
            L("Romantic dinner on deck at sunset", "Makan malam romantis di dek saat matahari terbenam"),
            L("Quiet beaches and a relaxed pace", "Pantai yang tenang dan ritme yang santai"),
            L("Optional photographer, hotel or villa stay", "Pilihan fotografer, menginap di hotel atau villa"),
        ],
        "see": ["packages/honeymoon.html", "services/stays.html", "services/yacht-boat-phinisi/vvip.html"],
    },
    "experiences/anniversary": {
        "img": ("packages", "anniversary"),
        "lead": L("Celebrate your years together somewhere unforgettable.",
                  "Rayakan tahun-tahun kebersamaan Anda di tempat yang tak terlupakan."),
        "paras": [
            L("An anniversary deserves more than a nice dinner. We plan a private trip with the moments that matter to you, from a surprise set-up on board to a table for two under the stars.",
              "Sebuah anniversary layak dirayakan lebih dari sekadar makan malam. Kami merencanakan trip pribadi dengan momen yang berarti bagi Anda, dari kejutan di atas kapal hingga meja untuk berdua di bawah bintang."),
            L("Tell us the date and what you have in mind, and we will arrange everything quietly in advance.",
              "Beri tahu kami tanggalnya dan apa yang Anda bayangkan, dan kami akan mengatur semuanya secara diam-diam sebelumnya."),
        ],
        "points": [
            L("Private yacht and a route chosen for you", "Yacht pribadi dan rute yang dipilih khusus untuk Anda"),
            L("Decorations, cake and a special dinner", "Dekorasi, kue, dan makan malam istimewa"),
            L("Surprise moments planned in advance", "Momen kejutan yang direncanakan sebelumnya"),
            L("Optional photographer to capture the day", "Pilihan fotografer untuk mengabadikan momen"),
        ],
        "see": ["packages/anniversary.html", "packages/honeymoon.html", "services/stays.html"],
    },
    "experiences/corporate-event": {
        "img": ("packages", "corporate-event"),
        "lead": L("Team trips, incentive travel and company events, planned end to end.",
                  "Trip tim, perjalanan insentif, dan acara perusahaan, direncanakan dari awal hingga akhir."),
        "paras": [
            L("Moving a group through Komodo takes careful coordination: flights, hotels, boats, transport and a schedule that works for everyone. We handle all of it as one plan.",
              "Membawa rombongan menjelajahi Komodo membutuhkan koordinasi yang cermat: penerbangan, hotel, kapal, transportasi, dan jadwal yang sesuai untuk semua orang. Kami menangani semuanya dalam satu rencana."),
            L("You get a single point of contact before and during the event, and a team on the ground making sure each part runs on time.",
              "Anda mendapatkan satu kontak sebelum dan selama acara, serta tim di lapangan yang memastikan setiap bagian berjalan tepat waktu."),
        ],
        "points": [
            L("Boats and hotels for groups of any size", "Kapal dan hotel untuk rombongan berbagai ukuran"),
            L("Group transport and airport transfers", "Transportasi rombongan dan transfer bandara"),
            L("Team activities, dinners and event set-ups", "Aktivitas tim, makan malam, dan persiapan acara"),
            L("One point of contact for the whole trip", "Satu kontak untuk seluruh perjalanan"),
        ],
        "see": ["packages/corporate-event.html", "services/ground-transportation.html", "services/stays.html"],
    },
}
