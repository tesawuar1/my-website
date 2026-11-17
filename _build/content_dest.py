# -*- coding: utf-8 -*-
"""Destination content (English + Indonesian).

Each destination page answers the same six questions. Edit the text here,
then run `python _build/build.py` to regenerate the site.

Photos: drop a photo at assets/img/destinations/<slug>.jpg and the build
uses it automatically. Until then the "pic" crop of a stand-in photo is used.
"""


def L(en, id_):
    return {"en": en, "id": id_}


# Section headings. {name} is replaced with the destination name.
DEST_HEADINGS = [
    ("what", L("What Is {name}", "Apa Itu {name}")),
    ("where", L("Where Is {name}", "Di Mana Letak {name}")),
    ("why", L("Why {name} Is a Must-Visit", "Mengapa {name} Wajib Dikunjungi")),
    ("expect", L("What to Expect in {name}", "Apa yang Menanti di {name}")),
    ("best", L("Best Time to Visit {name}", "Waktu Terbaik Mengunjungi {name}")),
    ("todo", L("Things to Do in {name}", "Aktivitas di {name}")),
]

DRY_SEASON = L(
    "The dry season, from about April to November, brings calm seas, clear water and sunny days.",
    "Musim kemarau, sekitar April hingga November, membawa laut yang tenang, air jernih, dan hari yang cerah.",
)

DESTINATIONS = [
    {
        "slug": "komodo-island",
        "name": L("Komodo Island", "Pulau Komodo"),
        "short": L("Home of the Komodo dragon", "Rumah sang komodo"),
        "pic": ("komodo-dragon", "50% 35%", "cover"),
        "what": L(
            "Komodo Island is the island that gave the national park, and the world's largest lizard, its name. "
            "Its dry hills, savanna and mangrove-lined bays are home to wild Komodo dragons, along with deer, "
            "wild boar and many bird species.",
            "Pulau Komodo adalah pulau yang memberi nama pada taman nasional ini, sekaligus pada kadal terbesar di dunia. "
            "Bukit-bukit kering, sabana, dan teluk berbakau di pulau ini menjadi rumah bagi komodo liar, "
            "bersama rusa, babi hutan, dan beragam jenis burung.",
        ),
        "where": L(
            "Komodo Island lies in the west of Komodo National Park, East Nusa Tenggara, between Sumbawa and Flores. "
            "Boats leave from Labuan Bajo on Flores. The crossing takes around 3 to 4 hours by phinisi, "
            "or about 1.5 to 2 hours by speedboat, depending on the sea.",
            "Pulau Komodo terletak di bagian barat Taman Nasional Komodo, Nusa Tenggara Timur, di antara Sumbawa dan Flores. "
            "Kapal berangkat dari Labuan Bajo di Pulau Flores. Perjalanan memakan waktu sekitar 3 sampai 4 jam dengan phinisi, "
            "atau sekitar 1,5 sampai 2 jam dengan speedboat, tergantung kondisi laut.",
        ),
        "why": L(
            "It is one of the very few places on earth where you can see Komodo dragons in their natural habitat. "
            "Walking the island with a ranger, close to animals that have lived here for millions of years, "
            "is the moment many guests remember long after the trip.",
            "Ini adalah salah satu dari sedikit tempat di dunia di mana Anda bisa melihat komodo di habitat aslinya. "
            "Berjalan menyusuri pulau bersama ranger, dekat dengan hewan yang telah hidup di sini selama jutaan tahun, "
            "menjadi momen yang paling diingat banyak tamu.",
        ),
        "expect": L(
            "Visits start at the Loh Liang ranger station, and a park ranger leads every walk. "
            "Trails of different lengths pass through dry forest and open savanna. Expect heat, little shade and dusty paths. "
            "The dragons are wild, so sightings are likely but never guaranteed.",
            "Kunjungan dimulai di pos ranger Loh Liang, dan setiap trekking selalu didampingi ranger taman nasional. "
            "Jalur dengan berbagai panjang melewati hutan kering dan sabana terbuka. Udara akan terasa panas, minim tempat teduh, dan jalurnya berdebu. "
            "Komodo adalah hewan liar, jadi kemungkinan besar Anda akan melihatnya, namun tidak selalu dijamin.",
        ),
        "best": L(
            "The dry season, from about April to November, brings calmer seas and easier treks. "
            "April to June is a lovely time, when the hills are still green. Mornings are cooler and the dragons are often more active. "
            "From December to March, rain and stronger waves can change boat routes.",
            "Musim kemarau, sekitar April hingga November, membawa laut yang lebih tenang dan trekking yang lebih nyaman. "
            "April hingga Juni adalah waktu yang indah, saat perbukitan masih hijau. Pagi hari lebih sejuk dan komodo sering lebih aktif. "
            "Dari Desember hingga Maret, hujan dan ombak yang lebih besar dapat mengubah rute kapal.",
        ),
        "todo": [
            L("Join a ranger-guided trek to see Komodo dragons in the wild", "Ikuti trekking bersama ranger untuk melihat komodo di alam liar"),
            L("Hike to a hilltop viewpoint over the bay", "Mendaki ke titik pandang di atas bukit dengan pemandangan teluk"),
            L("Visit Kampung Komodo, the island's fishing village", "Mengunjungi Kampung Komodo, desa nelayan di pulau ini"),
            L("Look out for deer, wild boar and the yellow-crested cockatoo", "Mengamati rusa, babi hutan, dan kakatua jambul kuning"),
            L("Combine your visit with nearby Pink Beach", "Lanjutkan perjalanan ke Pink Beach yang berada tidak jauh"),
        ],
    },
    {
        "slug": "pink-beach",
        "name": L("Pink Beach", "Pink Beach"),
        "short": L("Soft pink sand and coral", "Pasir merah muda dan terumbu karang"),
        "pic": ("padar-island", "92% 72%", "260%"),
        "what": L(
            "Pink Beach is one of only a handful of pink-sand beaches in the world. "
            "Its soft blush colour comes from tiny fragments of red organisms that live on the coral reef, mixed with white sand.",
            "Pink Beach adalah salah satu dari sedikit pantai berpasir merah muda di dunia. "
            "Warna merah mudanya berasal dari serpihan kecil organisme merah yang hidup di terumbu karang, bercampur dengan pasir putih.",
        ),
        "where": L(
            "Pink Beach is on Komodo Island, inside Komodo National Park. "
            "It is usually visited on the same day as the Komodo dragon trek, around 3 to 4 hours from Labuan Bajo by phinisi "
            "or about 2 hours by speedboat.",
            "Pink Beach berada di Pulau Komodo, di dalam kawasan Taman Nasional Komodo. "
            "Biasanya dikunjungi di hari yang sama dengan trekking komodo, sekitar 3 sampai 4 jam dari Labuan Bajo dengan phinisi "
            "atau sekitar 2 jam dengan speedboat.",
        ),
        "why": L(
            "The colour is at its best in bright sunlight and in the shallows, and the reef starts just a few metres from the shore. "
            "It is a rare chance to swim, snorkel and relax on a beach that looks like nowhere else.",
            "Warnanya paling indah saat matahari bersinar terang dan di area air dangkal, dan terumbu karang dimulai hanya beberapa meter dari bibir pantai. "
            "Kesempatan langka untuk berenang, snorkeling, dan bersantai di pantai yang tidak ada duanya.",
        ),
        "expect": L(
            "A quiet, curved beach with clear, shallow water and healthy coral close in. "
            "There are no shops or facilities, so bring water, sun protection and reef-safe sunscreen. "
            "The pink tone is subtle in places and strongest where the waves wash over the sand.",
            "Pantai yang tenang dan melengkung dengan air jernih yang dangkal serta terumbu karang yang sehat di dekat pantai. "
            "Tidak ada toko maupun fasilitas, jadi bawalah air minum, pelindung matahari, dan sunscreen yang ramah terumbu karang. "
            "Warna merah mudanya samar di beberapa bagian dan paling terlihat di tempat ombak menyapu pasir.",
        ),
        "best": L(
            "Visit in the dry season, from about April to November, for calm water and good visibility. "
            "Late morning to midday, when the sun is high, brings out the pink colour best.",
            "Kunjungi saat musim kemarau, sekitar April hingga November, untuk air yang tenang dan jarak pandang yang baik. "
            "Menjelang siang, saat matahari tinggi, warna merah muda pasirnya paling terlihat.",
        ),
        "todo": [
            L("Snorkel the reef just off the beach", "Snorkeling di terumbu karang tepat di depan pantai"),
            L("Swim in calm, clear water", "Berenang di air yang tenang dan jernih"),
            L("Take photos of the pink shoreline from the boat", "Mengabadikan garis pantai merah muda dari atas kapal"),
            L("Relax on the sand between island visits", "Bersantai di atas pasir di sela kunjungan antarpulau"),
        ],
    },
    {
        "slug": "padar-island",
        "name": L("Padar Island", "Pulau Padar"),
        "short": L("The famous three-bay view", "Pemandangan tiga teluk yang terkenal"),
        "pic": ("padar-island", "50% 55%", "cover"),
        "what": L(
            "Padar Island is the third-largest island in Komodo National Park and its most photographed. "
            "From the summit, three curved bays with white, black and pink-tinted sand sweep between steep, grassy ridges.",
            "Pulau Padar adalah pulau terbesar ketiga di Taman Nasional Komodo sekaligus yang paling sering difoto. "
            "Dari puncaknya, tiga teluk melengkung berpasir putih, hitam, dan merah muda terbentang di antara punggung bukit yang curam dan berumput.",
        ),
        "where": L(
            "Padar lies between Komodo Island and Rinca Island, in the middle of the national park. "
            "It takes around 1 hour by speedboat or 3 to 4 hours by phinisi from Labuan Bajo. "
            "Many multi-day trips anchor nearby overnight so guests can reach the trail at dawn.",
            "Pulau Padar terletak di antara Pulau Komodo dan Pulau Rinca, di tengah kawasan taman nasional. "
            "Perjalanannya sekitar 1 jam dengan speedboat atau 3 sampai 4 jam dengan phinisi dari Labuan Bajo. "
            "Banyak trip menginap yang membuang jangkar di dekatnya agar tamu bisa mulai mendaki saat fajar.",
        ),
        "why": L(
            "The view from the top is one of the most famous in Indonesia, and it is even better in person. "
            "Watching the sun rise over the three bays, with the islands of the park spread out around you, "
            "is a highlight of any Komodo trip.",
            "Pemandangan dari puncaknya adalah salah satu yang paling terkenal di Indonesia, dan jauh lebih indah jika dilihat langsung. "
            "Menyaksikan matahari terbit di atas tiga teluk, dengan pulau-pulau taman nasional terbentang di sekeliling Anda, "
            "menjadi momen puncak dari perjalanan ke Komodo.",
        ),
        "expect": L(
            "A path of stone and wooden steps climbs to the main viewpoint in about 30 to 45 minutes. "
            "It is steep and exposed, so come early, wear good shoes and carry water. "
            "Rangers are on the island, and the trail can be busy around sunrise.",
            "Jalur berundak dari batu dan kayu mengantar Anda ke titik pandang utama dalam waktu sekitar 30 sampai 45 menit. "
            "Jalurnya cukup curam dan terbuka, jadi datanglah lebih pagi, kenakan alas kaki yang nyaman, dan bawa air minum. "
            "Ranger berjaga di pulau ini, dan jalurnya bisa cukup ramai menjelang matahari terbit.",
        ),
        "best": L(
            "Sunrise is the classic time, with cooler air and soft light. "
            "The hills are green around April and May, and turn golden from July onwards. "
            "The dry season, from about April to November, offers the clearest skies.",
            "Matahari terbit adalah waktu favorit, dengan udara sejuk dan cahaya yang lembut. "
            "Perbukitan berwarna hijau sekitar April dan Mei, lalu berubah keemasan mulai Juli. "
            "Musim kemarau, sekitar April hingga November, menawarkan langit paling cerah.",
        ),
        "todo": [
            L("Hike to the summit for sunrise", "Mendaki ke puncak untuk menyaksikan matahari terbit"),
            L("Photograph the three bays from the viewpoint", "Memotret tiga teluk dari titik pandang"),
            L("Return for a quieter sunset hike", "Kembali untuk pendakian sore yang lebih sepi"),
            L("See the coloured-sand beaches from the boat", "Melihat pantai berpasir warna-warni dari atas kapal"),
        ],
    },
    {
        "slug": "sebayur-island",
        "name": L("Sebayur Island", "Pulau Sebayur"),
        "short": L("Calm water and coral gardens", "Air tenang dan taman karang"),
        "pic": ("padar-island", "18% 88%", "260%"),
        "what": L(
            "Sebayur is a small, quiet island with soft white sand and calm turquoise water. "
            "It is popular for easy snorkeling and relaxing between bigger sights, and a gentle hill offers views over the nearby islands.",
            "Sebayur adalah pulau kecil yang tenang dengan pasir putih yang lembut dan air biru toska yang tenang. "
            "Pulau ini populer untuk snorkeling santai dan beristirahat di sela kunjungan ke tempat lain, dan bukit kecilnya menawarkan pemandangan pulau-pulau di sekitarnya.",
        ),
        "where": L(
            "Sebayur sits close to Labuan Bajo, on the edge of Komodo National Park, roughly 1 to 1.5 hours away by boat. "
            "It is often included on day trips or as a calm stop on the way back to port.",
            "Sebayur berada tidak jauh dari Labuan Bajo, di tepi kawasan Taman Nasional Komodo, sekitar 1 sampai 1,5 jam perjalanan dengan kapal. "
            "Pulau ini sering menjadi bagian dari trip sehari atau tempat singgah yang tenang dalam perjalanan pulang ke pelabuhan.",
        ),
        "why": L(
            "It is a relaxed, uncrowded place with colourful coral close to the shore, "
            "which makes it ideal for beginners, families and anyone who wants a slower moment in the day.",
            "Suasananya santai dan tidak ramai, dengan terumbu karang berwarna-warni yang dekat dengan pantai. "
            "Cocok untuk pemula, keluarga, dan siapa saja yang ingin menikmati waktu lebih santai.",
        ),
        "expect": L(
            "Shallow, easy entry from the beach, colourful coral and plenty of reef fish. "
            "Facilities are limited, which keeps the island peaceful.",
            "Akses masuk ke laut yang mudah dan dangkal dari pantai, karang berwarna-warni, dan banyak ikan karang. "
            "Fasilitasnya terbatas, sehingga suasana pulau tetap tenang.",
        ),
        "best": L(
            DRY_SEASON["en"] + " Mornings usually have the calmest water.",
            DRY_SEASON["id"] + " Pagi hari biasanya airnya paling tenang.",
        ),
        "todo": [
            L("Snorkel the coral garden off the beach", "Snorkeling di taman karang depan pantai"),
            L("Walk up the hill for a view of the islands", "Berjalan ke atas bukit untuk melihat pemandangan pulau"),
            L("Swim and relax on the white sand", "Berenang dan bersantai di pasir putih"),
            L("Enjoy lunch on board in the sheltered bay", "Menikmati makan siang di kapal di teluk yang terlindung"),
        ],
    },
    {
        "slug": "batu-bolong",
        "name": L("Batu Bolong", "Batu Bolong"),
        "short": L("One of Komodo's richest dive sites", "Salah satu titik selam terbaik di Komodo"),
        "pic": ("padar-island", "96% 50%", "320%"),
        "what": L(
            "Batu Bolong, meaning \"hollow rock\", is a small rocky pinnacle that rises from the sea with a hole through its top. "
            "Underwater it is one of the richest dive sites in Komodo, covered in hard and soft coral and surrounded by huge schools of fish.",
            "Batu Bolong, yang berarti \"batu berlubang\", adalah bongkahan batu karang kecil yang menjulang dari laut dengan lubang di bagian atasnya. "
            "Di bawah air, ini adalah salah satu titik selam terkaya di Komodo, dipenuhi karang keras dan lunak serta dikelilingi kawanan ikan yang sangat besar.",
        ),
        "where": L(
            "It lies in the central part of the national park, in the channel between Komodo Island and Tatawa Island, "
            "about 2 to 3 hours from Labuan Bajo by boat.",
            "Batu Bolong terletak di bagian tengah taman nasional, di selat antara Pulau Komodo dan Pulau Tatawa, "
            "sekitar 2 sampai 3 jam dari Labuan Bajo dengan kapal.",
        ),
        "why": L(
            "Strong currents on both sides have helped keep the coral in remarkable condition. "
            "Divers often see turtles, reef sharks, Napoleon wrasse and dense clouds of colourful reef fish.",
            "Arus kuat di kedua sisinya membantu menjaga kondisi terumbu karang tetap luar biasa. "
            "Penyelam sering melihat penyu, hiu karang, ikan napoleon, dan kawanan ikan karang berwarna-warni yang sangat padat.",
        ),
        "expect": L(
            "Currents can be very strong, so Batu Bolong is best for experienced divers and is only visited at the right tide. "
            "Snorkeling is possible at slack water in the sheltered area, always with a guide.",
            "Arus di sini bisa sangat kuat, sehingga Batu Bolong paling cocok untuk penyelam berpengalaman dan hanya dikunjungi saat pasang surut yang tepat. "
            "Snorkeling dapat dilakukan saat arus tenang di area yang terlindung, selalu dengan pemandu.",
        ),
        "best": L(
            "Dives are planned around each day's tide. Visibility is often best in the dry season, from about April to November.",
            "Penyelaman direncanakan sesuai pasang surut setiap harinya. Jarak pandang biasanya paling baik saat musim kemarau, sekitar April hingga November.",
        ),
        "todo": [
            L("Dive the coral walls with an experienced guide", "Menyelam di dinding karang bersama pemandu berpengalaman"),
            L("Snorkel the sheltered side at slack tide", "Snorkeling di sisi yang terlindung saat arus tenang"),
            L("Look for turtles, reef sharks and Napoleon wrasse", "Mencari penyu, hiu karang, dan ikan napoleon"),
            L("Try underwater photography", "Mencoba fotografi bawah air"),
        ],
    },
    {
        "slug": "manta-point",
        "name": L("Manta Point", "Manta Point"),
        "short": L("Swim with manta rays", "Berenang bersama pari manta"),
        "pic": ("padar-island", "62% 96%", "300%"),
        "what": L(
            "Manta Point is a shallow reef area where reef manta rays gather to feed and visit cleaning stations. "
            "Swimming alongside these graceful animals, often wider than you are tall, is a highlight of Komodo for many guests.",
            "Manta Point adalah kawasan terumbu dangkal tempat pari manta karang berkumpul untuk makan dan dibersihkan oleh ikan-ikan kecil. "
            "Berenang bersama hewan anggun ini, yang lebar sayapnya sering melebihi tinggi badan Anda, menjadi momen favorit banyak tamu.",
        ),
        "where": L(
            "Also known as Karang Makassar, it lies east of Komodo Island near the Taka Makassar sandbank, "
            "about 2 hours from Labuan Bajo by speedboat.",
            "Dikenal juga sebagai Karang Makassar, lokasinya berada di sebelah timur Pulau Komodo, dekat gosong pasir Taka Makassar, "
            "sekitar 2 jam dari Labuan Bajo dengan speedboat.",
        ),
        "why": L(
            "Few places let you see manta rays this easily from the surface. You do not need to dive: confident swimmers can see them while snorkeling.",
            "Tidak banyak tempat di mana Anda bisa melihat pari manta semudah ini dari permukaan. Anda tidak perlu menyelam: perenang yang percaya diri bisa melihatnya sambil snorkeling.",
        ),
        "expect": L(
            "Snorkeling here is usually a drift: the boat drops you up-current, you float with the water and are picked up further along. "
            "Currents can be strong, so life jackets and a guide are recommended. "
            "Mantas are wild, and sightings vary from day to day.",
            "Snorkeling di sini biasanya dilakukan dengan cara drift: kapal menurunkan Anda di hulu arus, Anda mengapung mengikuti arus, lalu dijemput di titik berikutnya. "
            "Arusnya bisa kuat, jadi pelampung dan pemandu sangat disarankan. "
            "Pari manta adalah hewan liar, dan kemunculannya berbeda setiap hari.",
        ),
        "best": L(
            "Mantas can be seen year-round. Numbers change with tides, currents and plankton, so your guide plans the visit around conditions on the day.",
            "Pari manta dapat dilihat sepanjang tahun. Jumlahnya dipengaruhi pasang surut, arus, dan plankton, sehingga pemandu akan mengatur waktu kunjungan sesuai kondisi hari itu.",
        ),
        "todo": [
            L("Drift-snorkel with manta rays", "Drift snorkeling bersama pari manta"),
            L("Dive the cleaning stations", "Menyelam di area tempat manta dibersihkan"),
            L("Watch for turtles and reef sharks", "Mengamati penyu dan hiu karang"),
            L("Combine with a stop at Taka Makassar", "Lanjutkan dengan singgah di Taka Makassar"),
        ],
    },
    {
        "slug": "kelor-island",
        "name": L("Kelor Island", "Pulau Kelor"),
        "short": L("A short hike, a wide view", "Pendakian singkat, pemandangan luas"),
        "pic": ("padar-island", "12% 42%", "300%"),
        "what": L(
            "Kelor is a small island with a steep hill, a white-sand beach and clear water, and is often the first stop on a Komodo trip. "
            "The short climb rewards you with a wide view over the bay and the islands beyond.",
            "Kelor adalah pulau kecil dengan bukit yang curam, pantai berpasir putih, dan air yang jernih, dan sering menjadi persinggahan pertama dalam perjalanan ke Komodo. "
            "Pendakian singkatnya terbayar dengan pemandangan luas ke arah teluk dan pulau-pulau di sekitarnya.",
        ),
        "where": L(
            "Kelor is one of the closest islands to Labuan Bajo, around 30 to 45 minutes by boat.",
            "Kelor adalah salah satu pulau terdekat dari Labuan Bajo, sekitar 30 sampai 45 menit dengan kapal.",
        ),
        "why": L(
            "It is close, easy to fit into any route and offers one of the best views for the effort. "
            "It is a beautiful way to start your days at sea.",
            "Lokasinya dekat, mudah dimasukkan ke rute mana pun, dan menawarkan pemandangan yang sangat sepadan dengan usahanya. "
            "Cara yang indah untuk memulai hari di laut.",
        ),
        "expect": L(
            "The trail to the top is short but steep and sandy, with loose ground near the summit, so good shoes help. "
            "Below, the reef off the beach is good for snorkeling.",
            "Jalur menuju puncak memang pendek, tetapi curam dan berpasir, dengan tanah yang gembur di dekat puncak, jadi alas kaki yang baik akan sangat membantu. "
            "Di bawahnya, terumbu karang di depan pantai cocok untuk snorkeling.",
        ),
        "best": L(
            "Early morning or late afternoon, when the air is cooler and the light is soft. " + DRY_SEASON["en"],
            "Pagi hari atau sore hari, saat udara lebih sejuk dan cahayanya lembut. " + DRY_SEASON["id"],
        ),
        "todo": [
            L("Hike to the hilltop viewpoint", "Mendaki ke titik pandang di puncak bukit"),
            L("Snorkel off the beach", "Snorkeling di depan pantai"),
            L("Swim in the clear shallows", "Berenang di perairan dangkal yang jernih"),
            L("Take photos of the bay from above", "Memotret teluk dari ketinggian"),
        ],
    },
    {
        "slug": "taka-makassar",
        "name": L("Taka Makassar", "Taka Makassar"),
        "short": L("A sandbank in turquoise water", "Gosong pasir di tengah laut biru toska"),
        "pic": ("padar-island", "30% 96%", "250%"),
        "what": L(
            "Taka Makassar is a curved sandbank that rises out of the sea at low tide, surrounded by bright turquoise water. "
            "With no trees or buildings, it feels like a tiny island of pure white sand.",
            "Taka Makassar adalah gosong pasir melengkung yang muncul dari laut saat air surut, dikelilingi air biru toska yang cerah. "
            "Tanpa pepohonan maupun bangunan, tempat ini terasa seperti pulau mungil dari pasir putih.",
        ),
        "where": L(
            "It lies close to Manta Point (Karang Makassar), east of Komodo Island, about 2 hours from Labuan Bajo by speedboat.",
            "Lokasinya dekat dengan Manta Point (Karang Makassar), di sebelah timur Pulau Komodo, sekitar 2 jam dari Labuan Bajo dengan speedboat.",
        ),
        "why": L(
            "It is one of the most striking sights in the park and pairs perfectly with snorkeling at Manta Point nearby.",
            "Ini adalah salah satu pemandangan paling memukau di taman nasional dan sangat pas dikombinasikan dengan snorkeling di Manta Point yang berada di dekatnya.",
        ),
        "expect": L(
            "How much sand you see depends on the tide; at high tide it can almost disappear. "
            "There is no shade, so bring sun protection. The shallow water around it is calm and great for swimming.",
            "Luas pasir yang terlihat bergantung pada pasang surut; saat air pasang, gosong ini bisa hampir hilang. "
            "Tidak ada tempat berteduh, jadi bawalah pelindung matahari. Perairan dangkal di sekitarnya tenang dan cocok untuk berenang.",
        ),
        "best": L(
            "Low tide, in the dry season. We plan the timing around tide tables for your travel date.",
            "Saat air surut di musim kemarau. Kami mengatur waktunya berdasarkan jadwal pasang surut pada tanggal perjalanan Anda.",
        ),
        "todo": [
            L("Walk along the sandbank", "Berjalan menyusuri gosong pasir"),
            L("Swim in the turquoise shallows", "Berenang di perairan dangkal biru toska"),
            L("Take photos from the water and the sand", "Berfoto dari air maupun dari atas pasir"),
            L("Snorkel nearby at Manta Point", "Snorkeling di Manta Point yang berada di dekatnya"),
        ],
    },
    {
        "slug": "kanawa-island",
        "name": L("Kanawa Island", "Pulau Kanawa"),
        "short": L("A peaceful island with an easy reef", "Pulau tenang dengan terumbu yang mudah dijangkau"),
        "pic": ("padar-island", "78% 78%", "230%"),
        "what": L(
            "Kanawa is a small, peaceful island with a long wooden jetty, white sand and one of the easiest house reefs in the area. "
            "It is a favourite place to slow down after the busier sights.",
            "Kanawa adalah pulau kecil yang tenang dengan dermaga kayu yang panjang, pasir putih, dan terumbu karang yang paling mudah dijangkau di kawasan ini. "
            "Tempat favorit untuk bersantai setelah mengunjungi lokasi-lokasi yang lebih ramai.",
        ),
        "where": L(
            "Kanawa sits north-west of Labuan Bajo, around 1 to 1.5 hours by boat, on the edge of Komodo National Park.",
            "Kanawa terletak di sebelah barat laut Labuan Bajo, sekitar 1 sampai 1,5 jam dengan kapal, di tepi kawasan Taman Nasional Komodo.",
        ),
        "why": L(
            "You can snorkel straight from the jetty, often with turtles, starfish and plenty of reef fish. "
            "There is also a small island resort, so you can stay for lunch, sunset or the night.",
            "Anda bisa langsung snorkeling dari dermaga, sering kali bersama penyu, bintang laut, dan banyak ikan karang. "
            "Di pulau ini juga ada resor kecil, sehingga Anda bisa singgah untuk makan siang, menikmati matahari terbenam, atau menginap.",
        ),
        "expect": L(
            "Clear, shallow water right off the jetty with coral, blue starfish and frequent turtles. "
            "A relaxed atmosphere with a restaurant on the island.",
            "Air jernih dan dangkal tepat di depan dermaga dengan karang, bintang laut biru, dan penyu yang sering terlihat. "
            "Suasananya santai, dengan restoran di pulau.",
        ),
        "best": L(
            DRY_SEASON["en"] + " Mornings usually have the clearest water.",
            DRY_SEASON["id"] + " Pagi hari biasanya airnya paling jernih.",
        ),
        "todo": [
            L("Snorkel from the jetty", "Snorkeling langsung dari dermaga"),
            L("Swim with sea turtles", "Berenang bersama penyu"),
            L("Walk up for a sunset view", "Berjalan ke atas untuk menikmati matahari terbenam"),
            L("Stay overnight at the island resort", "Menginap di resor pulau"),
        ],
    },
    {
        "slug": "siaba-island",
        "name": L("Siaba Island", "Pulau Siaba"),
        "short": L("Snorkel with sea turtles", "Snorkeling bersama penyu"),
        "pic": ("padar-island", "8% 70%", "290%"),
        "what": L(
            "Siaba is a small island with a sheltered bay known for its sea turtles. "
            "The calm, shallow water and seagrass make it one of the most reliable places in the park to snorkel with green turtles.",
            "Siaba adalah pulau kecil dengan teluk terlindung yang terkenal dengan penyunya. "
            "Air yang tenang, dangkal, dan padang lamunnya menjadikan tempat ini salah satu lokasi paling andal di taman nasional untuk snorkeling bersama penyu hijau.",
        ),
        "where": L(
            "Siaba lies inside Komodo National Park, about 2 hours from Labuan Bajo by boat, and fits easily into a day or multi-day route.",
            "Siaba berada di dalam kawasan Taman Nasional Komodo, sekitar 2 jam dari Labuan Bajo dengan kapal, dan mudah dimasukkan ke rute sehari maupun beberapa hari.",
        ),
        "why": L(
            "Seeing turtles graze peacefully a few metres below you is unforgettable, and the gentle conditions suit almost everyone.",
            "Melihat penyu makan dengan tenang beberapa meter di bawah Anda adalah pengalaman yang tak terlupakan, dan kondisi airnya yang tenang cocok untuk hampir semua orang.",
        ),
        "expect": L(
            "Calm conditions most of the time, so it suits beginners and families. "
            "Please keep a respectful distance and never touch the turtles.",
            "Kondisi air hampir selalu tenang, sehingga cocok untuk pemula dan keluarga. "
            "Mohon jaga jarak dan jangan pernah menyentuh penyu.",
        ),
        "best": L(
            DRY_SEASON["en"] + " Mornings are usually calmest.",
            DRY_SEASON["id"] + " Pagi hari biasanya paling tenang.",
        ),
        "todo": [
            L("Snorkel with green turtles", "Snorkeling bersama penyu hijau"),
            L("Swim in the sheltered bay", "Berenang di teluk yang terlindung"),
            L("Take underwater photos", "Berfoto di bawah air"),
            L("Relax on deck between swims", "Bersantai di dek kapal di sela berenang"),
        ],
    },
    {
        "slug": "rinca-island",
        "name": L("Rinca Island", "Pulau Rinca"),
        "short": L("Dragons, savanna and wildlife", "Komodo, sabana, dan satwa liar"),
        "pic": ("komodo-dragon", "25% 75%", "190%"),
        "what": L(
            "Rinca Island is the second-largest island in Komodo National Park and one of the best places to see Komodo dragons. "
            "Its open savanna, palm-dotted hills and mangroves are also home to macaques, water buffalo and deer.",
            "Pulau Rinca adalah pulau terbesar kedua di Taman Nasional Komodo dan salah satu tempat terbaik untuk melihat komodo. "
            "Sabana terbuka, perbukitan dengan pohon lontar, dan hutan bakaunya juga menjadi rumah bagi monyet, kerbau liar, dan rusa.",
        ),
        "where": L(
            "Rinca lies between Komodo Island and Flores, closer to Labuan Bajo: about 1 hour by speedboat or 2 hours by phinisi. "
            "Visits start at the Loh Buaya ranger station.",
            "Pulau Rinca terletak di antara Pulau Komodo dan Flores, lebih dekat ke Labuan Bajo: sekitar 1 jam dengan speedboat atau 2 jam dengan phinisi. "
            "Kunjungan dimulai di pos ranger Loh Buaya.",
        ),
        "why": L(
            "Rinca is easier to reach than Komodo Island and offers excellent chances to see dragons, "
            "which makes it ideal for shorter trips or for seeing a second side of the park.",
            "Pulau Rinca lebih mudah dijangkau dibanding Pulau Komodo dan memberikan peluang besar untuk melihat komodo, "
            "sehingga cocok untuk perjalanan singkat atau untuk melihat sisi lain dari taman nasional.",
        ),
        "expect": L(
            "A ranger guides every walk. The area around the ranger station has elevated boardwalks, and short treks continue into the savanna. "
            "It is hot and dry, so bring a hat and water.",
            "Setiap trekking didampingi ranger. Area di sekitar pos ranger dilengkapi jalur papan yang ditinggikan, dan trekking singkat berlanjut ke sabana. "
            "Udaranya panas dan kering, jadi bawalah topi dan air minum.",
        ),
        "best": L(
            DRY_SEASON["en"] + " Visit in the morning, when it is cooler and the dragons are often more active.",
            DRY_SEASON["id"] + " Datanglah pagi hari, saat udara lebih sejuk dan komodo sering lebih aktif.",
        ),
        "todo": [
            L("Take a ranger-guided trek to see Komodo dragons", "Trekking bersama ranger untuk melihat komodo"),
            L("Spot macaques, water buffalo and deer", "Mengamati monyet, kerbau liar, dan rusa"),
            L("Walk up to a hilltop viewpoint", "Berjalan ke titik pandang di atas bukit"),
            L("Cruise past the mangroves by boat", "Menyusuri hutan bakau dengan kapal"),
        ],
    },
    {
        "slug": "kalong-island",
        "name": L("Kalong Island", "Pulau Kalong"),
        "short": L("Thousands of flying foxes at sunset", "Ribuan kalong saat matahari terbenam"),
        "pic": ("padar-island", "50% 12%", "260%"),
        "what": L(
            "Kalong means \"flying fox\" in Indonesian. This small mangrove island is home to a large colony of fruit bats, "
            "and every evening at sunset thousands of them take to the sky.",
            "Kalong adalah nama lain dari kelelawar buah besar. Pulau bakau kecil ini menjadi rumah bagi koloni kalong yang sangat besar, "
            "dan setiap sore saat matahari terbenam, ribuan kalong terbang memenuhi langit.",
        ),
        "where": L(
            "Kalong lies near Rinca Island, in the east of the national park, about 2 hours from Labuan Bajo by boat. "
            "Many overnight boats anchor nearby to watch the show.",
            "Pulau Kalong berada dekat Pulau Rinca, di bagian timur taman nasional, sekitar 2 jam dari Labuan Bajo dengan kapal. "
            "Banyak kapal menginap yang membuang jangkar di dekatnya untuk menyaksikan pertunjukan alam ini.",
        ),
        "why": L(
            "Watching the sky fill with bats against a golden sunset is one of the most memorable natural sights in Komodo.",
            "Menyaksikan langit dipenuhi kalong dengan latar matahari terbenam keemasan adalah salah satu pemandangan alam paling berkesan di Komodo.",
        ),
        "expect": L(
            "You watch from the boat; there is no landing on the island. "
            "The bats start leaving at dusk and stream overhead toward the larger islands to feed, usually for 20 to 30 minutes.",
            "Anda menyaksikannya dari atas kapal; tidak ada pendaratan di pulau ini. "
            "Kalong mulai terbang saat senja dan melintas di atas kepala menuju pulau-pulau besar untuk mencari makan, biasanya selama 20 sampai 30 menit.",
        ),
        "best": L(
            "At sunset, any time of year. The dry season, from about April to November, offers the calmest anchorages.",
            "Saat matahari terbenam, kapan saja sepanjang tahun. Musim kemarau, sekitar April hingga November, menawarkan tempat berlabuh yang paling tenang.",
        ),
        "todo": [
            L("Watch the flying foxes take flight", "Menyaksikan ribuan kalong terbang"),
            L("Enjoy the sunset from the deck", "Menikmati matahari terbenam dari dek kapal"),
            L("Have dinner on deck under the stars", "Makan malam di dek di bawah bintang"),
            L("Take silhouette photos at dusk", "Memotret siluet saat senja"),
        ],
    },
    {
        "slug": "manjarite-island",
        "name": L("Manjarite Island", "Pulau Manjarite"),
        "short": L("Gentle snorkeling, clear water", "Snorkeling santai, air jernih"),
        "pic": ("padar-island", "88% 92%", "270%"),
        "what": L(
            "Manjarite is a quiet spot with calm, clear water and colourful coral gardens close to the surface, "
            "one of the gentler snorkeling sites in Komodo.",
            "Manjarite adalah tempat yang tenang dengan air jernih dan taman karang berwarna-warni yang dekat dengan permukaan, "
            "salah satu lokasi snorkeling paling bersahabat di Komodo.",
        ),
        "where": L(
            "Manjarite lies in the east of the national park, near Rinca and Kalong islands, about 1.5 to 2 hours from Labuan Bajo. "
            "It is often visited in the afternoon, before sunset at Kalong.",
            "Manjarite terletak di bagian timur taman nasional, dekat Pulau Rinca dan Pulau Kalong, sekitar 1,5 sampai 2 jam dari Labuan Bajo. "
            "Tempat ini sering dikunjungi sore hari, sebelum menikmati matahari terbenam di Pulau Kalong.",
        ),
        "why": L(
            "Healthy coral, good visibility and usually calm water make it a great choice for relaxed snorkeling, with fewer crowds than the famous sites.",
            "Karang yang sehat, jarak pandang yang baik, dan air yang biasanya tenang menjadikannya pilihan tepat untuk snorkeling santai, dengan pengunjung yang lebih sedikit dibanding lokasi terkenal lainnya.",
        ),
        "expect": L(
            "A shallow reef with plenty of fish, close to a small beach. Conditions suit beginners and confident swimmers alike.",
            "Terumbu dangkal dengan banyak ikan, dekat dengan pantai kecil. Kondisinya cocok untuk pemula maupun perenang yang sudah percaya diri.",
        ),
        "best": L(
            DRY_SEASON["en"] + " Afternoon light makes the water glow.",
            DRY_SEASON["id"] + " Cahaya sore membuat airnya tampak berkilau.",
        ),
        "todo": [
            L("Snorkel the shallow coral garden", "Snorkeling di taman karang dangkal"),
            L("Swim in calm, clear water", "Berenang di air yang tenang dan jernih"),
            L("Relax on the small beach", "Bersantai di pantai kecil"),
            L("Continue to Kalong Island for sunset", "Lanjut ke Pulau Kalong untuk menikmati matahari terbenam"),
        ],
    },
]
