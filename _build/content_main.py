# -*- coding: utf-8 -*-
"""Site-wide content: contacts, interface text, services, packages and pages.

Edit text here, then run `python _build/build.py` to regenerate the site.
"""

from content_dest import L

CONTACT = {
    "email_enquiry": "hello@komodoandko.com",
    "email_partner": "partnership@komodoandko.com",
    "whatsapp_display": "0823-3929-7918",
    "whatsapp_intl": "6282339297918",  # used for wa.me links
    # Google Apps Script "Web app" URL that saves enquiries to the Google Sheet and emails
    # the team. Leave empty until it is set up (see tools/google-apps-script/SETUP.md).
    "enquiry_endpoint": "https://script.google.com/macros/s/AKfycbwAu16ED6XwP_X-eK7sjr0NGnXa_NaIHLO1YoNd0I9fbTSJi1jLTbuAZWJqrkD0bza85A/exec",
    "social": [
        ("Instagram", "https://www.instagram.com/komodoandko"),
        ("TikTok", "https://www.tiktok.com/@komodoandko"),
        ("Facebook", "https://www.facebook.com/komodoandko"),
        ("YouTube", "https://www.youtube.com/@komodoandko"),
    ],
}

UI = {
    "nav_services": L("Concierge Service", "Layanan Concierge"),
    "nav_packages": L("Package", "Paket"),
    "nav_destinations": L("Destination", "Destinasi"),
    "nav_enquiry": L("Enquiry", "Hubungi Kami"),
    "all_services": L("All concierge services", "Semua layanan concierge"),
    "all_packages": L("All packages", "Semua paket"),
    "all_destinations": L("All destinations", "Semua destinasi"),
    "plan_now": L("Plan Now", "Rencanakan Sekarang"),
    "send_enquiry": L("Send an enquiry", "Kirim permintaan"),
    "menu": L("Menu", "Menu"),
    "close": L("Close", "Tutup"),
    "home": L("Home", "Beranda"),
    "view": L("View", "Lihat"),
    "learn_more": L("Learn more", "Selengkapnya"),
    "view_all": L("View all", "Lihat semua"),
    "legal_note": L(
        "",
        "Dokumen ini disediakan dalam bahasa Inggris, yang merupakan versi resmi dan berlaku. Hubungi tim kami jika Anda memerlukan penjelasan dalam bahasa Indonesia.",
    ),
    "on_this_page": L("On this page", "Di halaman ini"),
    "more_destinations": L("More destinations", "Destinasi lainnya"),
    "other_packages": L("Other packages", "Paket lainnya"),
    "price": L("Price", "Harga"),
    "price_on_request": L("On request", "Sesuai permintaan"),
    "duration": L("Duration", "Durasi"),
    "boat": L("Boat", "Kapal"),
    "trip_type": L("Trip type", "Jenis trip"),
    "sample_route": L("Sample itinerary", "Contoh itinerary"),
    "sample_note": L(
        "This is a sample route. We adjust the final plan to the weather, tides, season and what you would like to see.",
        "Ini adalah contoh rute. Rencana akhir kami sesuaikan dengan cuaca, pasang surut, musim, dan keinginan Anda.",
    ),
    "typically_includes": L("Typically includes", "Biasanya sudah termasuk"),
    "includes_note": L(
        "The exact inclusions are confirmed in your personal quote.",
        "Rincian fasilitas yang termasuk akan dikonfirmasi dalam penawaran pribadi Anda.",
    ),
    "day": L("Day", "Hari"),
    "cta_title": L("Ready to plan your Komodo journey?", "Siap merencanakan perjalanan Anda ke Komodo?"),
    "cta_text": L(
        "Tell us your dates, your group and what you would love to do. We will reply with a plan made for you.",
        "Ceritakan tanggal perjalanan, jumlah rombongan, dan apa yang ingin Anda lakukan. Kami akan membalas dengan rencana yang dibuat khusus untuk Anda.",
    ),
    "footer_tagline": L(
        "Concierge service for Komodo National Park and Labuan Bajo.",
        "Layanan concierge untuk Taman Nasional Komodo dan Labuan Bajo.",
    ),
    "footer_enquiry": L("Enquiries", "Pertanyaan & pemesanan"),
    "footer_partner": L("Partnerships", "Kerja sama"),
    "footer_follow": L("Follow us", "Ikuti kami"),
    "footer_explore": L("Explore", "Jelajahi"),
    "privacy": L("Privacy Policy", "Kebijakan Privasi"),
    "terms": L("Terms & Conditions", "Syarat & Ketentuan"),
    "about": L("About Us", "Tentang Kami"),
    "rights": L("All rights reserved.", "Hak cipta dilindungi."),
    "lang_label": L("Language", "Bahasa"),
    "scroll": L("Scroll to explore", "Gulir untuk menjelajah"),
    "hud_park": L("Komodo National Park", "Taman Nasional Komodo"),
    "discover": L("Discover", "Jelajahi"),
    "view_package": L("View package", "Lihat paket"),
    "prev": L("Previous", "Sebelumnya"),
    "next": L("Next", "Berikutnya"),
    "hero_label": L("Komodo National Park, Indonesia", "Taman Nasional Komodo, Indonesia"),
    "promise": L("Our promise", "Janji kami"),
    "chat_wa": L("Chat on WhatsApp", "Chat via WhatsApp"),
    "dd_packages": L(
        "Private charters, sharing trips and celebrations at sea.",
        "Sewa kapal pribadi, sharing trip, dan perayaan di laut.",
    ),
    "dd_destinations": L(
        "Thirteen places we know well, from the summit of Padar to the reefs of Batu Bolong.",
        "Tiga belas tempat yang kami kenal dengan baik, dari puncak Padar hingga terumbu Batu Bolong.",
    ),
}

# ---------------------------------------------------------------------------
# Concierge services
# ---------------------------------------------------------------------------
SERVICES = [
    {
        "slug": "yacht-boat-phinisi",
        "name": L("Yacht, Boat & Phinisi", "Yacht, Kapal & Phinisi"),
        "short": L(
            "From crewed luxury phinisi to fast speedboats, the right boat for your group.",
            "Dari phinisi mewah lengkap dengan kru hingga speedboat cepat, kapal yang tepat untuk rombongan Anda.",
        ),
        "pic": ("padar-island", "70% 70%", "200%"),
        "intro": L(
            "The boat shapes your whole trip. We match you with a vessel that fits your group, your style and your budget, "
            "and we handle the booking, the crew briefing and the route.",
            "Kapal menentukan pengalaman perjalanan Anda. Kami mencarikan kapal yang sesuai dengan rombongan, gaya perjalanan, dan anggaran Anda, "
            "lalu mengurus pemesanan, koordinasi dengan kru, hingga rutenya.",
        ),
        "items": [
            ("vvip", L("VVIP", "VVIP"), L(
                "Our most exclusive phinisi yachts: spacious suites, a dedicated crew and chef, and a route planned entirely around you.",
                "Phinisi paling eksklusif kami: kabin suite yang luas, kru dan chef khusus, serta rute yang sepenuhnya disesuaikan untuk Anda.",
            )),
            ("vip", L("VIP", "VIP"), L(
                "Elegant phinisi with private cabins, attentive crew and comfortable decks to relax on between islands.",
                "Phinisi elegan dengan kabin pribadi, kru yang sigap, dan dek yang nyaman untuk bersantai di sela perjalanan antarpulau.",
            )),
            ("deluxe", L("Deluxe", "Deluxe"), L(
                "Comfortable, good-value boats with private cabins, a relaxed way to explore the park over one or more nights.",
                "Kapal yang nyaman dan bernilai baik dengan kabin pribadi, cara santai untuk menjelajahi taman nasional selama satu malam atau lebih.",
            )),
            ("speedboat", L("Speedboat", "Speedboat"), L(
                "See more of the park in a single day. Ideal for day trips, tight schedules and early starts at Padar.",
                "Kunjungi lebih banyak tempat dalam satu hari. Cocok untuk trip sehari, jadwal yang padat, dan berangkat pagi ke Padar.",
            )),
        ],
    },
    {
        "slug": "experiences",
        "name": L("Experiences", "Pengalaman"),
        "short": L(
            "Island hopping, snorkeling, diving and celebrations, arranged around you.",
            "Island hopping, snorkeling, diving, hingga perayaan istimewa, diatur sesuai keinginan Anda.",
        ),
        "pic": ("padar-island", "40% 85%", "230%"),
        "intro": L(
            "Every guest comes to Komodo for something different. Tell us what matters to you and we will build the days around it, "
            "with trusted guides, dive centres and crews.",
            "Setiap tamu datang ke Komodo dengan tujuan yang berbeda. Ceritakan apa yang penting bagi Anda, dan kami akan menyusun hari-hari Anda di sekitarnya, "
            "bersama pemandu, pusat selam, dan kru terpercaya.",
        ),
        "items": [
            ("island-hopping", L("Island Hopping", "Island Hopping"), L(
                "Padar, Komodo, Pink Beach and quieter islands in between, in an order that avoids the crowds.",
                "Padar, Komodo, Pink Beach, dan pulau-pulau yang lebih sepi di antaranya, dengan urutan yang menghindari keramaian.",
            )),
            ("snorkeling", L("Snorkeling", "Snorkeling"), L(
                "Manta rays, turtles and coral gardens, with a guide who knows the tides and the best spots.",
                "Pari manta, penyu, dan taman karang, bersama pemandu yang memahami pasang surut dan lokasi terbaik.",
            )),
            ("diving", L("Diving", "Diving"), L(
                "Fun dives and courses with established dive centres, from gentle reefs to world-class current dives.",
                "Fun dive dan kursus selam bersama pusat selam terpercaya, dari terumbu yang tenang hingga titik selam berarus kelas dunia.",
            )),
            ("water-activities", L("Water Activities", "Aktivitas Air"), L(
                "Kayaking, paddleboarding and swimming stops, added wherever the water is calm.",
                "Kayak, paddleboard, dan berenang, ditambahkan di setiap lokasi dengan air yang tenang.",
            )),
            ("honeymoon", L("Honeymoon", "Honeymoon"), L(
                "Private yachts, sunset dinners on deck and quiet beaches for two.",
                "Yacht pribadi, makan malam saat matahari terbenam di dek, dan pantai yang tenang hanya untuk berdua.",
            )),
            ("anniversary", L("Anniversary", "Anniversary"), L(
                "A celebration at sea, with decorations, a special dinner and moments planned in advance.",
                "Perayaan di atas laut, lengkap dengan dekorasi, makan malam istimewa, dan momen yang sudah direncanakan.",
            )),
            ("corporate-event", L("Corporate Event", "Corporate Event"), L(
                "Team trips, incentive travel and events, with boats, transport and schedules coordinated for the whole group.",
                "Trip tim, perjalanan insentif, dan acara perusahaan, dengan kapal, transportasi, dan jadwal yang dikoordinasikan untuk seluruh rombongan.",
            )),
        ],
    },
    {
        "slug": "stays",
        "name": L("Stays", "Akomodasi"),
        "short": L(
            "Hotels and villas in Labuan Bajo, chosen to match your trip.",
            "Hotel dan villa di Labuan Bajo, dipilih sesuai perjalanan Anda.",
        ),
        "pic": ("padar-island", "55% 30%", "240%"),
        "intro": L(
            "Where you stay before and after your time at sea matters. We recommend and book places we know well, "
            "and time your check-in and check-out around your boat.",
            "Tempat menginap sebelum dan sesudah perjalanan laut sangatlah penting. Kami merekomendasikan dan memesan tempat yang kami kenal dengan baik, "
            "serta menyesuaikan waktu check-in dan check-out dengan jadwal kapal Anda.",
        ),
        "items": [
            ("hotel", L("Hotel", "Hotel"), L(
                "From boutique hotels to resorts with sea views, with transfers to the harbour arranged.",
                "Dari hotel butik hingga resor dengan pemandangan laut, termasuk pengaturan transfer ke pelabuhan.",
            )),
            ("villa", L("Villa", "Villa"), L(
                "Private villas for families, groups and couples who want space and privacy.",
                "Villa pribadi untuk keluarga, rombongan, dan pasangan yang menginginkan ruang dan privasi.",
            )),
        ],
    },
    {
        "slug": "ground-transportation",
        "name": L("Ground Transportation", "Transportasi Darat"),
        "short": L(
            "Airport pick-ups, private drivers and group transport in Labuan Bajo.",
            "Penjemputan bandara, sopir pribadi, dan transportasi rombongan di Labuan Bajo.",
        ),
        "pic": ("padar-island", "30% 45%", "250%"),
        "intro": L(
            "Arrive, transfer and move between the airport, your hotel and the harbour without thinking about it. "
            "Every ride is timed to your flights and your boat.",
            "Tiba, berpindah, dan bepergian antara bandara, hotel, dan pelabuhan tanpa perlu memikirkannya. "
            "Setiap perjalanan disesuaikan dengan jadwal penerbangan dan kapal Anda.",
        ),
        "items": [
            ("luxury-vehicles", L("Luxury & Premium Vehicles", "Kendaraan Mewah & Premium"), L(
                "Comfortable, well-kept premium cars for a smooth arrival and departure.",
                "Mobil premium yang nyaman dan terawat untuk kedatangan dan keberangkatan yang lancar.",
            )),
            ("group-transportation", L("Group Transportation", "Transportasi Rombongan"), L(
                "Vans and buses for families, groups and corporate events, with luggage handled.",
                "Van dan bus untuk keluarga, rombongan, dan acara perusahaan, termasuk penanganan bagasi.",
            )),
            ("private-transfers", L("Private Transfers & Chauffeur", "Transfer Pribadi & Sopir Pribadi"), L(
                "Private transfers and a dedicated driver for your days on land.",
                "Transfer pribadi dan sopir khusus selama Anda berada di darat.",
            )),
        ],
    },
    {
        "slug": "itinerary-design",
        "name": L("Itinerary Design & Booking", "Perancangan Itinerary & Pemesanan"),
        "short": L(
            "A personal Komodo itinerary, designed, booked and coordinated for you.",
            "Itinerary Komodo pribadi, dirancang, dipesan, dan dikoordinasikan untuk Anda.",
        ),
        "pic": ("padar-island", "50% 60%", "160%"),
        "intro": L(
            "We help you design a personalised Komodo itinerary based on your travel dates, interests, preferences and budget. "
            "From choosing the right experiences and arranging bookings to coordinating the details, we take care of it.",
            "Kami membantu Anda merancang itinerary Komodo pribadi berdasarkan tanggal perjalanan, minat, preferensi, dan anggaran Anda. "
            "Mulai dari memilih pengalaman yang tepat, mengatur pemesanan, hingga mengoordinasikan setiap detailnya, semuanya kami urus.",
        ),
        "steps": True,
        "items": [
            ("share", L("Share your plans", "Ceritakan rencana Anda"), L(
                "Send us your dates, group size, interests and budget through the enquiry form or WhatsApp.",
                "Kirimkan tanggal perjalanan, jumlah rombongan, minat, dan anggaran Anda melalui formulir enquiry atau WhatsApp.",
            )),
            ("design", L("We design the itinerary", "Kami merancang itinerary"), L(
                "We suggest a route, a boat, stays and experiences that fit, and adjust it with you until it feels right.",
                "Kami menyarankan rute, kapal, akomodasi, dan pengalaman yang sesuai, lalu menyesuaikannya bersama Anda hingga terasa pas.",
            )),
            ("book", L("We book everything", "Kami memesan semuanya"), L(
                "Boats, hotels, transfers, guides and activities are confirmed with partners we trust.",
                "Kapal, hotel, transfer, pemandu, dan aktivitas dikonfirmasi bersama mitra yang kami percaya.",
            )),
            ("coordinate", L("We coordinate on the ground", "Kami berkoordinasi di lapangan"), L(
                "During your trip we stay in touch with the crew and drivers, and adapt plans if the weather changes.",
                "Selama perjalanan, kami tetap berkoordinasi dengan kru dan sopir, serta menyesuaikan rencana jika cuaca berubah.",
            )),
        ],
    },
]

# ---------------------------------------------------------------------------
# Packages
# ---------------------------------------------------------------------------
INCLUDES_BOAT = [
    L("Boat with captain and crew", "Kapal beserta kapten dan kru"),
    L("Meals on board, drinking water, coffee and tea", "Makan di kapal, air minum, kopi, dan teh"),
    L("Snorkeling equipment", "Peralatan snorkeling"),
    L("Pick-up and drop-off in Labuan Bajo", "Antar-jemput di Labuan Bajo"),
    L("Trip coordination before and during your journey", "Koordinasi perjalanan sebelum dan selama trip"),
]

PACKAGES = [
    {
        "slug": "private-trip",
        "home": True,
        "name": L("Private Trip", "Private Trip"),
        "pic": ("padar-island", "62% 62%", "190%"),
        "duration": L("2 days, 1 night", "2 hari 1 malam"),
        "boat": L("Private yacht charter", "Sewa yacht pribadi"),
        "type": L("Private", "Private"),
        "price": None,
        "intro": L(
            "A private yacht charter for 2 days and 1 night, just for you and your group. "
            "Sail at your own pace, wake up near Padar for sunrise and see the highlights of the park without sharing the deck.",
            "Sewa yacht pribadi selama 2 hari 1 malam, hanya untuk Anda dan rombongan. "
            "Berlayar sesuai ritme Anda, bangun di dekat Padar untuk menyaksikan matahari terbit, dan nikmati destinasi terbaik taman nasional tanpa berbagi kapal.",
        ),
        "days": [
            L("Labuan Bajo pick-up, Kelor Island hike and snorkel, Rinca Island dragon trek, sunset at Kalong Island and overnight on board.",
              "Penjemputan di Labuan Bajo, mendaki dan snorkeling di Pulau Kelor, trekking komodo di Pulau Rinca, matahari terbenam di Pulau Kalong, dan menginap di kapal."),
            L("Sunrise hike on Padar Island, Pink Beach, Komodo Island trek, Taka Makassar and Manta Point, then back to Labuan Bajo.",
              "Pendakian matahari terbit di Pulau Padar, Pink Beach, trekking di Pulau Komodo, Taka Makassar dan Manta Point, lalu kembali ke Labuan Bajo."),
        ],
        "includes": INCLUDES_BOAT,
    },
    {
        "slug": "sharing-trip",
        "home": True,
        "name": L("Sharing Trip", "Sharing Trip"),
        "pic": ("padar-island", "20% 80%", "220%"),
        "duration": L("3 days, 2 nights", "3 hari 2 malam"),
        "boat": L("Shared yacht", "Yacht bersama"),
        "type": L("Sharing", "Sharing"),
        "price": L("From USD 300 per person", "Mulai USD 300 per orang"),
        "intro": L(
            "Join other travellers on a yacht for 3 days and 2 nights. "
            "It is a great-value way to see the best of Komodo, with your own cabin and the crew taking care of everything.",
            "Bergabung bersama wisatawan lain di atas yacht selama 3 hari 2 malam. "
            "Cara hemat untuk menikmati keindahan terbaik Komodo, dengan kabin sendiri dan kru yang mengurus semuanya.",
        ),
        "days": [
            L("Labuan Bajo pick-up, Kelor Island, snorkeling at Manjarite and sunset at Kalong Island.",
              "Penjemputan di Labuan Bajo, Pulau Kelor, snorkeling di Manjarite, dan matahari terbenam di Pulau Kalong."),
            L("Padar Island sunrise, Pink Beach, Komodo Island trek, Taka Makassar and Manta Point.",
              "Matahari terbit di Pulau Padar, Pink Beach, trekking di Pulau Komodo, Taka Makassar, dan Manta Point."),
            L("Turtles at Siaba Island, Kanawa Island, then back to Labuan Bajo in the afternoon.",
              "Melihat penyu di Pulau Siaba, Pulau Kanawa, lalu kembali ke Labuan Bajo pada sore hari."),
        ],
        "includes": INCLUDES_BOAT,
    },
    {
        "slug": "one-day-trip",
        "home": True,
        "name": L("1 Day Trip", "1 Day Trip"),
        "pic": ("padar-island", "50% 40%", "180%"),
        "duration": L("1 day", "1 hari"),
        "boat": L("Speedboat", "Speedboat"),
        "type": L("Private or sharing", "Private atau sharing"),
        "price": None,
        "options": [
            (L("Private speedboat", "Speedboat private"), L(
                "The whole speedboat for your group, with timing and stops adjusted to you.",
                "Satu speedboat penuh untuk rombongan Anda, dengan waktu dan tujuan yang disesuaikan.",
            )),
            (L("Sharing speedboat", "Speedboat sharing"), L(
                "Join a small group on a fixed route, a great-value way to see the highlights in a day.",
                "Bergabung dengan rombongan kecil dengan rute yang sudah ditentukan, cara hemat untuk melihat destinasi utama dalam sehari.",
            )),
        ],
        "intro": L(
            "See the highlights of Komodo National Park in a single day by speedboat. "
            "Choose a private boat for your group, or join a sharing trip.",
            "Nikmati destinasi utama Taman Nasional Komodo dalam satu hari dengan speedboat. "
            "Pilih kapal pribadi untuk rombongan Anda, atau bergabung dengan sharing trip.",
        ),
        "days": [
            L("Early departure from Labuan Bajo, Padar Island hike, Pink Beach, Komodo Island trek, Taka Makassar, Manta Point and Kanawa Island, back by late afternoon.",
              "Berangkat pagi dari Labuan Bajo, mendaki Pulau Padar, Pink Beach, trekking di Pulau Komodo, Taka Makassar, Manta Point, dan Pulau Kanawa, kembali menjelang sore."),
        ],
        "includes": [
            L("Speedboat with captain and crew", "Speedboat beserta kapten dan kru"),
            L("Lunch, drinking water and snacks", "Makan siang, air minum, dan camilan"),
            L("Snorkeling equipment", "Peralatan snorkeling"),
            L("Hotel pick-up and drop-off in Labuan Bajo", "Antar-jemput hotel di Labuan Bajo"),
        ],
    },
    {
        "slug": "3d2n",
        "home": True,
        "name": L("3D2N Trip", "Trip 3D2N"),
        "pic": ("padar-island", "85% 40%", "240%"),
        "duration": L("3 days, 2 nights", "3 hari 2 malam"),
        "boat": L("Phinisi or yacht", "Phinisi atau yacht"),
        "type": L("Private", "Private"),
        "price": None,
        "intro": L(
            "Three days and two nights at sea is the ideal length for most guests: enough time to see the famous sights, "
            "swim with turtles and mantas, and still have slow moments on deck.",
            "Tiga hari dua malam di laut adalah durasi yang ideal bagi sebagian besar tamu: cukup waktu untuk melihat tempat-tempat terkenal, "
            "berenang bersama penyu dan pari manta, sekaligus menikmati waktu santai di dek.",
        ),
        "days": [
            L("Labuan Bajo pick-up, Kelor Island, Rinca Island dragon trek and sunset at Kalong Island.",
              "Penjemputan di Labuan Bajo, Pulau Kelor, trekking komodo di Pulau Rinca, dan matahari terbenam di Pulau Kalong."),
            L("Padar Island sunrise, Pink Beach, Komodo Island, Taka Makassar and Manta Point.",
              "Matahari terbit di Pulau Padar, Pink Beach, Pulau Komodo, Taka Makassar, dan Manta Point."),
            L("Siaba Island turtles, Kanawa Island, then back to Labuan Bajo.",
              "Penyu di Pulau Siaba, Pulau Kanawa, lalu kembali ke Labuan Bajo."),
        ],
        "includes": INCLUDES_BOAT,
    },
    {
        "slug": "4d3n",
        "home": True,
        "name": L("4D3N Trip", "Trip 4D3N"),
        "pic": ("padar-island", "10% 55%", "260%"),
        "duration": L("4 days, 3 nights", "4 hari 3 malam"),
        "boat": L("Phinisi or yacht", "Phinisi atau yacht"),
        "type": L("Private", "Private"),
        "price": None,
        "intro": L(
            "Four days lets you explore further and at a slower pace, adding quieter islands, more time in the water "
            "and dives at sites like Batu Bolong.",
            "Empat hari memberi Anda waktu untuk menjelajah lebih jauh dengan ritme yang lebih santai, termasuk pulau-pulau yang lebih sepi, lebih banyak waktu di air, "
            "dan menyelam di titik seperti Batu Bolong.",
        ),
        "days": [
            L("Labuan Bajo pick-up, Kelor Island and Manjarite, sunset at Kalong Island.",
              "Penjemputan di Labuan Bajo, Pulau Kelor dan Manjarite, matahari terbenam di Pulau Kalong."),
            L("Rinca Island trek, Padar Island sunset hike and a quiet anchorage overnight.",
              "Trekking di Pulau Rinca, pendakian sore di Pulau Padar, dan bermalam di tempat berlabuh yang tenang."),
            L("Pink Beach, Komodo Island, Batu Bolong, Taka Makassar and Manta Point.",
              "Pink Beach, Pulau Komodo, Batu Bolong, Taka Makassar, dan Manta Point."),
            L("Siaba Island turtles, Sebayur or Kanawa Island, then back to Labuan Bajo.",
              "Penyu di Pulau Siaba, Pulau Sebayur atau Kanawa, lalu kembali ke Labuan Bajo."),
        ],
        "includes": INCLUDES_BOAT,
    },
    {
        "slug": "honeymoon",
        "name": L("Honeymoon Package", "Paket Honeymoon"),
        "pic": ("padar-island", "78% 88%", "240%"),
        "duration": L("Flexible", "Fleksibel"),
        "boat": L("Private yacht", "Yacht pribadi"),
        "type": L("Private", "Private"),
        "price": None,
        "intro": L(
            "A private journey for two: a yacht to yourselves, sunrise on Padar, quiet beaches and dinner on deck as the sun goes down. "
            "We take care of every detail so you can simply enjoy each other.",
            "Perjalanan pribadi untuk berdua: yacht hanya untuk Anda, matahari terbit di Padar, pantai yang tenang, dan makan malam di dek saat matahari terbenam. "
            "Kami mengurus setiap detailnya agar Anda bisa menikmati kebersamaan.",
        ),
        "highlights": [
            L("Private yacht with a cabin prepared for two", "Yacht pribadi dengan kabin yang disiapkan untuk berdua"),
            L("Romantic dinner on deck at sunset", "Makan malam romantis di dek saat matahari terbenam"),
            L("Padar sunrise and quiet beach stops", "Matahari terbit di Padar dan singgah di pantai yang sepi"),
            L("Optional photographer and hotel or villa stay", "Pilihan fotografer serta menginap di hotel atau villa"),
        ],
    },
    {
        "slug": "anniversary",
        "name": L("Anniversary Package", "Paket Anniversary"),
        "pic": ("padar-island", "40% 30%", "220%"),
        "duration": L("Flexible", "Fleksibel"),
        "boat": L("Private yacht", "Yacht pribadi"),
        "type": L("Private", "Private"),
        "price": None,
        "intro": L(
            "Celebrate your years together somewhere unforgettable. We plan a private trip with the moments that matter to you, "
            "from a surprise set-up on board to a special dinner under the stars.",
            "Rayakan tahun-tahun kebersamaan Anda di tempat yang tak terlupakan. Kami merencanakan perjalanan pribadi dengan momen-momen yang berarti bagi Anda, "
            "mulai dari kejutan di atas kapal hingga makan malam istimewa di bawah bintang.",
        ),
        "highlights": [
            L("Private yacht and a route chosen for you", "Yacht pribadi dan rute yang dipilih khusus untuk Anda"),
            L("Decorations, cake and a special dinner", "Dekorasi, kue, dan makan malam istimewa"),
            L("Surprise moments planned in advance", "Momen kejutan yang direncanakan sebelumnya"),
            L("Optional photographer to capture the day", "Pilihan fotografer untuk mengabadikan momen"),
        ],
    },
    {
        "slug": "corporate-event",
        "name": L("Corporate Event", "Corporate Event"),
        "pic": ("padar-island", "50% 75%", "170%"),
        "duration": L("Flexible", "Fleksibel"),
        "boat": L("One or more boats", "Satu atau beberapa kapal"),
        "type": L("Group", "Rombongan"),
        "price": None,
        "intro": L(
            "Team trips, incentive travel and company events in Komodo, planned end to end. "
            "We coordinate boats, hotels, transport and schedules for the whole group, and stay on hand throughout.",
            "Trip tim, perjalanan insentif, dan acara perusahaan di Komodo, direncanakan dari awal hingga akhir. "
            "Kami mengoordinasikan kapal, hotel, transportasi, dan jadwal untuk seluruh rombongan, serta selalu siap membantu selama acara.",
        ),
        "highlights": [
            L("Boats and hotels for groups of any size", "Kapal dan hotel untuk rombongan berbagai ukuran"),
            L("Group transport and airport transfers", "Transportasi rombongan dan transfer bandara"),
            L("Team activities, dinners and event set-ups", "Aktivitas tim, makan malam, dan persiapan acara"),
            L("One point of contact for the whole trip", "Satu kontak untuk seluruh perjalanan"),
        ],
    },
]

# ---------------------------------------------------------------------------
# Home page
# ---------------------------------------------------------------------------
HOME = {
    "title": L("Komodo & Ko. | Komodo Concierge Service", "Komodo & Ko. | Layanan Concierge Komodo"),
    "desc": L(
        "From planning and booking to coordinating every detail, we bring your Komodo journey together so you can travel with ease.",
        "Dari perencanaan dan pemesanan hingga koordinasi setiap detail, kami menyatukan perjalanan Komodo Anda agar Anda bisa bepergian dengan tenang.",
    ),
    "h1a": L("You Explore.", "Anda Menjelajah."),
    "h1b": L("We Handle the Rest", "Sisanya Kami yang Urus"),
    "tagline": L(
        "From planning and booking to coordinating every detail, we bring your Komodo journey together so you can travel with ease.",
        "Dari perencanaan dan pemesanan hingga koordinasi setiap detail, kami menyatukan perjalanan Komodo Anda agar Anda bisa bepergian dengan tenang.",
    ),
    "caption": L(
        "Padar Island, Komodo National Park<br>East Nusa Tenggara, Indonesia",
        "Pulau Padar, Taman Nasional Komodo<br>Nusa Tenggara Timur, Indonesia",
    ),
    "vision_lines": [
        L("One trusted team", "Satu tim terpercaya"),
        L("for your entire", "untuk seluruh"),
        L("Komodo journey", "perjalanan Komodo Anda"),
    ],
    "vision_p": L(
        "Yachts, stays, transfers and experiences, planned and coordinated by people who know these islands.",
        "Yacht, akomodasi, transfer, dan pengalaman, direncanakan dan dikoordinasikan oleh orang-orang yang mengenal pulau-pulau ini.",
    ),
    "acct": L(
        "We plan the route, book the boat and the rooms, time every transfer and stay in touch with the crew, so all you have to do is show up and look around.",
        "Kami merencanakan rute, memesan kapal dan kamar, mengatur waktu setiap transfer, dan terus berkoordinasi dengan kru, sehingga Anda cukup datang dan menikmati pemandangan.",
    ),
    "hotspots": [
        # (x, y) as fractions of the Padar photo
        (0.51, 0.58, L("Summit trail", "Jalur menuju puncak"), L("30 to 45 min hike", "Pendakian 30 sampai 45 menit")),
        (0.42, 0.76, L("Black-sand bay", "Teluk pasir hitam"), L("Seen from the top", "Terlihat dari puncak")),
        (0.71, 0.64, L("White-sand bay", "Teluk pasir putih"), L("Where the boats anchor", "Tempat kapal berlabuh")),
    ],
    "station_title": L("Komodo is wild. Your trip doesn't have to be.", "Komodo itu liar. Perjalanan Anda tidak harus begitu."),
    "station_p": L(
        "Five services, one point of contact. Choose what you need, or let us handle all of it.",
        "Lima layanan, satu kontak. Pilih yang Anda butuhkan, atau serahkan semuanya kepada kami.",
    ),
    "dragon_card_title": L("Komodo dragon", "Komodo"),
    "dragon_card_latin": "Varanus komodoensis",
    "dragon_len": L("up to 3 m long", "panjang hingga 3 m"),
    "dragon_note": L(
        "Found in the wild only on Komodo, Rinca, Flores and a few small nearby islands.",
        "Di alam liar hanya ditemukan di Komodo, Rinca, Flores, dan beberapa pulau kecil di sekitarnya.",
    ),
    "services_title": L("Concierge services", "Layanan concierge"),
    "services_p": L(
        "Everything you need for Komodo, arranged by one team.",
        "Semua yang Anda butuhkan untuk ke Komodo, diatur oleh satu tim.",
    ),
    "packages_title": L("Explore packages", "Jelajahi paket"),
    "destinations_title": L("Explore destinations", "Jelajahi destinasi"),
    "how_title": L("How it works", "Cara kerjanya"),
    "how_steps": [
        (L("Tell us your plans", "Ceritakan rencana Anda"), L(
            "Contact us via WhatsApp, DM, email or this enquiry form. Share your travel dates, number of guests and the experiences you're looking for.",
            "Hubungi kami melalui WhatsApp, DM, email, atau formulir enquiry ini. Ceritakan tanggal perjalanan, jumlah tamu, dan pengalaman yang Anda cari.",
        )),
        (L("Explore your options", "Jelajahi pilihan Anda"), L(
            "We'll recommend suitable services, experiences and itineraries based on your preferences and budget.",
            "Kami akan merekomendasikan layanan, pengalaman, dan itinerary yang sesuai dengan preferensi dan anggaran Anda.",
        )),
        (L("Receive your proposal", "Terima penawaran Anda"), L(
            "Review your personalised arrangements, pricing and itinerary before confirming.",
            "Tinjau rencana perjalanan, harga, dan itinerary yang disusun khusus untuk Anda sebelum mengonfirmasi.",
        )),
        (L("Confirm your booking", "Konfirmasi pemesanan"), L(
            "Once you're happy with the arrangements, proceed with payment to secure your booking.",
            "Setelah Anda setuju dengan rencananya, lanjutkan pembayaran untuk mengamankan pemesanan Anda.",
        )),
        (L("Enjoy the experience", "Nikmati perjalanan Anda"), L(
            "We'll coordinate your arrangements and keep you informed, so you can enjoy your journey with peace of mind.",
            "Kami akan mengoordinasikan semua rencana dan terus memberi kabar, sehingga Anda bisa menikmati perjalanan dengan tenang.",
        )),
    ],
    "why_title": L("Why choose us", "Mengapa memilih kami"),
    "why": [
        (L("Local experts", "Ahli lokal"), L(
            "We know these islands, the tides and the seasons, and we plan every route with that knowledge.",
            "Kami mengenal pulau-pulau ini, pasang surut, dan musimnya, dan setiap rute kami rencanakan berdasarkan pengetahuan tersebut.",
        )),
        (L("Trusted partner network", "Jaringan mitra terpercaya"), L(
            "We work with boats, hotels, guides and drivers we know personally and trust with our guests.",
            "Kami bekerja sama dengan kapal, hotel, pemandu, dan sopir yang kami kenal secara langsung dan kami percayai untuk melayani tamu kami.",
        )),
        (L("Time-saving convenience", "Praktis dan hemat waktu"), L(
            "One conversation instead of dozens of bookings. We handle the details while you enjoy the trip.",
            "Cukup satu percakapan, bukan puluhan pemesanan. Kami mengurus detailnya selagi Anda menikmati perjalanan.",
        )),
    ],
    "about_title": L("About Komodo & Ko.", "Tentang Komodo & Ko."),
    "about_p": L(
        "We are a concierge team for Komodo National Park and Labuan Bajo, bringing boats, stays, transport and experiences together into one easy journey.",
        "Kami adalah tim concierge untuk Taman Nasional Komodo dan Labuan Bajo, yang menyatukan kapal, akomodasi, transportasi, dan pengalaman menjadi satu perjalanan yang mudah.",
    ),
}

# ---------------------------------------------------------------------------
# Other pages
# ---------------------------------------------------------------------------
ENQUIRY = {
    "title": L("Enquiry", "Hubungi Kami"),
    "intro": L(
        "Tell us about your trip and we will reply with ideas and a personal quote. All fields are required.",
        "Ceritakan rencana perjalanan Anda dan kami akan membalas dengan ide serta penawaran pribadi. Semua kolom wajib diisi.",
    ),
    "next_title": L("What happens next", "Langkah selanjutnya"),
    "next": [
        L("Choose to send your enquiry by WhatsApp or email.", "Pilih untuk mengirim permintaan Anda melalui WhatsApp atau email."),
        L("We reply with questions, ideas and options.", "Kami membalas dengan pertanyaan, ide, dan pilihan."),
        L("Once you are happy, we confirm and book everything.", "Setelah Anda setuju, kami mengonfirmasi dan memesan semuanya."),
    ],
    "fields": {
        "name": (L("Name", "Nama"), L("e.g. John Smith", "contoh: John Smith")),
        "phone": (L("Phone / WhatsApp number", "Nomor telepon / WhatsApp"), L("e.g. +62 812 3456 7890", "contoh: +62 812 3456 7890")),
        "email": (L("Email", "Email"), L("e.g. johnsmith@gmail.com", "contoh: johnsmith@gmail.com")),
        "dates": (L("Travel dates", "Tanggal perjalanan"), L("Your travel date or preferred date range", "Tanggal perjalanan atau rentang tanggal yang Anda inginkan")),
        "guests": (L("Number of guests", "Jumlah tamu"), L("e.g. 2", "contoh: 2")),
        "service": (L("Service / preferred experience", "Layanan / pengalaman yang diinginkan"), L("What service and experience are you looking for?", "Layanan dan pengalaman apa yang Anda cari?")),
        "budget": (L("Estimated budget", "Perkiraan anggaran"), L("Your estimated budget for this trip", "Perkiraan anggaran Anda untuk perjalanan ini")),
    },
    "errors": {
        "required": L("Please fill in this field.", "Mohon isi kolom ini."),
        "email": L("Please enter a valid email address, e.g. johnsmith@gmail.com.", "Mohon masukkan alamat email yang valid, contoh: johnsmith@gmail.com."),
        "phone": L("Please enter a phone number with at least 8 digits.", "Mohon masukkan nomor telepon minimal 8 digit."),
        "guests": L("Please enter a number of at least 1.", "Mohon masukkan angka minimal 1."),
    },
    "send_wa": L("Send via WhatsApp", "Kirim via WhatsApp"),
    "send_email": L("Send via Email", "Kirim via Email"),
    "send_note": L(
        "Your WhatsApp or email app will open with your enquiry ready to send.",
        "Aplikasi WhatsApp atau email Anda akan terbuka dengan pesan yang siap dikirim.",
    ),
    "sent": L(
        "Your enquiry is ready in your WhatsApp or email app. Press send there, and we will reply as soon as we can.",
        "Pesan Anda sudah siap di aplikasi WhatsApp atau email. Tekan kirim di sana, dan kami akan segera membalas.",
    ),
    "msg_intro": L("Hello Komodo & Ko., I would like to plan a trip.", "Halo Komodo & Ko., saya ingin merencanakan perjalanan."),
    "msg_subject": L("Enquiry from", "Enquiry dari"),
}

ABOUT = {
    "title": L("About Us", "Tentang Kami"),
    "lead": L(
        "Komodo & Ko. is a concierge service for travellers visiting Komodo National Park and Labuan Bajo.",
        "Komodo & Ko. adalah layanan concierge bagi wisatawan yang berkunjung ke Taman Nasional Komodo dan Labuan Bajo.",
    ),
    "body": [
        L("Planning a trip to Komodo usually means talking to many different people: boat operators, hotels, drivers, dive centres and guides. "
          "We bring all of that together, so you have one team to talk to and one plan to follow.",
          "Merencanakan perjalanan ke Komodo biasanya berarti berkomunikasi dengan banyak pihak: operator kapal, hotel, sopir, pusat selam, dan pemandu. "
          "Kami menyatukan semuanya, sehingga Anda cukup berbicara dengan satu tim dan mengikuti satu rencana."),
        L("We know the islands, the seasons and the people who work here, and we choose our partners carefully. "
          "Whether you are planning a honeymoon, a family holiday or a corporate event, we design the trip around you and stay with you until you are home.",
          "Kami mengenal pulau-pulaunya, musimnya, dan orang-orang yang bekerja di sini, serta memilih mitra kami dengan cermat. "
          "Baik Anda merencanakan honeymoon, liburan keluarga, maupun acara perusahaan, kami merancang perjalanan sesuai kebutuhan Anda dan mendampingi Anda hingga kembali ke rumah."),
        L("Komodo & Ko. operates under PT Mountclaire Group Indonesia.",
          "Komodo & Ko. beroperasi di bawah naungan PT Mountclaire Group Indonesia."),
    ],
}

PRIVACY = {
    "title": L("Privacy Policy", "Kebijakan Privasi"),
    "sections": [
        (L("Information we collect", "Informasi yang kami kumpulkan"), L(
            "When you send an enquiry, we receive the details you share with us, such as your name, phone or WhatsApp number, email address, travel dates, number of guests, preferences and budget.",
            "Saat Anda mengirim permintaan, kami menerima data yang Anda bagikan, seperti nama, nomor telepon atau WhatsApp, alamat email, tanggal perjalanan, jumlah tamu, preferensi, dan anggaran.",
        )),
        (L("How we use it", "Cara kami menggunakannya"), L(
            "We use this information only to reply to you, plan and book your trip, and coordinate with the partners involved in your journey, such as boats, hotels and drivers.",
            "Kami menggunakan informasi ini hanya untuk membalas Anda, merencanakan dan memesan perjalanan Anda, serta berkoordinasi dengan mitra yang terlibat, seperti kapal, hotel, dan sopir.",
        )),
        (L("Sharing", "Berbagi informasi"), L(
            "We share only the details a partner needs to provide your service. We do not sell your personal information.",
            "Kami hanya membagikan data yang dibutuhkan mitra untuk memberikan layanan kepada Anda. Kami tidak menjual informasi pribadi Anda.",
        )),
        (L("Your choices", "Pilihan Anda"), L(
            "You can ask us at any time to see, correct or delete the information we hold about you by emailing hello@komodoandko.com.",
            "Anda dapat meminta kami kapan saja untuk melihat, memperbaiki, atau menghapus informasi tentang Anda dengan mengirim email ke hello@komodoandko.com.",
        )),
    ],
}

TERMS = {
    "title": L("Terms & Conditions", "Syarat & Ketentuan"),
    "sections": [
        (L("Bookings", "Pemesanan"), L(
            "A booking is confirmed once you accept our quote in writing and the requested deposit is received. Details of each booking are set out in your confirmation.",
            "Pemesanan dinyatakan terkonfirmasi setelah Anda menyetujui penawaran kami secara tertulis dan uang muka yang diminta telah diterima. Rincian setiap pemesanan tercantum dalam konfirmasi Anda.",
        )),
        (L("Payments and cancellations", "Pembayaran dan pembatalan"), L(
            "Payment schedules and cancellation terms depend on the services booked and are stated in your quote before you confirm.",
            "Jadwal pembayaran dan ketentuan pembatalan bergantung pada layanan yang dipesan dan dicantumkan dalam penawaran sebelum Anda mengonfirmasi.",
        )),
        (L("Weather and safety", "Cuaca dan keselamatan"), L(
            "Routes and activities at sea depend on weather, tides and national park rules. The captain and guides may change the plan for safety, and we will always look for the best alternative.",
            "Rute dan aktivitas di laut bergantung pada cuaca, pasang surut, dan peraturan taman nasional. Kapten dan pemandu dapat mengubah rencana demi keselamatan, dan kami akan selalu mencarikan alternatif terbaik.",
        )),
        (L("National park rules", "Peraturan taman nasional"), L(
            "Guests agree to follow the rules of Komodo National Park and the instructions of rangers and crew, including keeping a safe distance from wildlife.",
            "Tamu setuju untuk mematuhi peraturan Taman Nasional Komodo serta arahan ranger dan kru, termasuk menjaga jarak aman dari satwa liar.",
        )),
    ],
}
