import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum! Sana çevre kirliliğine karşı evde yapılabilecek şeyleri öğrenmen konusunda yardımcı olmak istiyorum senin için tavsiye verebilirim')

@bot.command()
async def hangi_konulara_sahipsin(ctx):
    await ctx.send(f'1-geri dönüşüm ve ayrıştırma bilgisi , 2-kompost yapmayı öğrenmek , 3-plastik kullanımı , 4-kendi temizlik ürünü yapmak , 5-yemek planlaması ve atık yönetimi , 6-enerji tasarufu sağlamak , 7-daha az tüketmek ve ikinci el eşyalar , 8-bilgi ve eğitimle farkındalık yaratmak')

@bot.command()
async def cozum1 (ctx):
    await ctx.send(f'Evde geri dönüşüm sürecini etkili bir şekilde yönetmek için öncelikle yerel geri dönüşüm kurallarını öğrenmelisiniz. Geri dönüştürülebilir materyallerin doğru bir şekilde ayrılması gerekir. Bu, kağıt, cam, plastik ve metal gibi malzemeleri ayrı kutularda biriktirmek anlamına gelir. Her belediyenin geri dönüşüm kuralları farklı olabilir, bu yüzden yerel yönetimlerin veya geri dönüşüm merkezlerinin sağladığı rehberlik ve bilgilere başvurabilirsiniz. Ayrıca, geri dönüşüm kutularının üzerine neyin geri dönüştürülebileceğini belirten etiketler koymak da faydalı olabilir.')

@bot.command()
async def cozum2 (ctx):
    await ctx.send(f'Kompost, organik atıkların (sebze-meyve kabukları, kahve telvesi, yumurta kabukları) doğal bir şekilde parçalanarak toprağa faydalı hale gelmesini sağlar. Bu, hem atık miktarını azaltır hem de bahçenizdeki toprağın kalitesini artırır. Kompost yaparken, nem dengesine dikkat etmek, havalandırmayı sağlamak ve uygun malzemeleri kullanmak önemlidir. Ayrıca, kompost kutuları veya torbaları kullanarak kompostlama sürecini daha düzenli ve kontrollü bir şekilde yönetebilirsiniz.')

@bot.command()
async def cozum3 (ctx):
    await ctx.send(f'Tek kullanımlık plastik ürünler çevreye büyük zarar verir. Bu yüzden, alışverişlerinizde plastik poşetler yerine yeniden kullanılabilir alışveriş torbaları kullanın. Plastik şişeler yerine, suyunuzu taşımak için metal veya cam şişeler tercih edin. Gıda saklama kaplarında da plastik yerine cam veya paslanmaz çelik ürünler kullanarak, hem sağlığınızı hem de çevreyi koruyabilirsiniz. Ayrıca, yiyeceklerinizi alırken ambalajlı ürünler yerine açık ürünleri tercih edebilir ve ambalajsız alışveriş yaparak plastik atıkları azaltabilirsiniz.')

@bot.command()
async def cozum4 (ctx):
    await ctx.send(f'Ev temizliğinde kimyasal temizlik ürünleri kullanmak yerine, doğal ve evde yapılabilecek temizlik ürünleri tercih edebilirsiniz. Sirke, karbonat, limon suyu gibi malzemeler, birçok temizlik işini etkili bir şekilde yapabilir. Örneğin, sirke ve su karışımı, cam temizliğinde kullanılabilirken, karbonat ve limon karışımı, lavaboların temizliğinde etkili olabilir. Bu şekilde, hem kimyasal maddelerden kaçınmış olursunuz hem de atık miktarınızı azaltabilirsiniz.')

@bot.command()
async def cozum5 (ctx):
    await ctx.send(f'Yemek pişirmeden önce bir plan yaparak, ihtiyaç duyduğunuz malzemeleri belirleyebilir ve bu sayede gereksiz alımlardan kaçınabilirsiniz. Artan yemekleri doğru bir şekilde saklamak ve gerektiğinde yeniden kullanmak da önemlidir. Artıkları yeniden değerlendirmek için, onları buzdolabında saklayabilir veya yeni tariflerde kullanabilirsiniz. Ayrıca, yemeklerinizi porsiyon kontrolü yaparak pişirmek, fazla yiyecek üretimini ve israfı azaltabilir')

@bot.command()
async def cozum6 (ctx):
    await ctx.send(f'Evde enerji ve su tüketimini azaltmak, hem faturalarınızı düşürebilir hem de çevreye katkıda bulunabilir. Enerji tasarruflu ampuller kullanmak, cihazları gereksiz yere açık bırakmamak ve enerji verimli cihazlar tercih etmek bu konuda atılacak önemli adımlardır. Su tasarrufu sağlamak için ise, duş sürelerini kısaltabilir, su tasarrufu sağlayan aparatlar kullanabilir ve sızıntıları hemen onarabilirsiniz.')
                   
@bot.command()
async def cozum7 (ctx):
    await ctx.send(f'Alışveriş alışkanlıklarınızı gözden geçirerek, yalnızca gerçekten ihtiyaç duyduğunuz ürünleri satın almaya özen gösterin. İkinci el eşyalar, hem bütçenizi korur hem de atık miktarını azaltır. Çevrim içi ikinci el pazarları veya yerel takas etkinlikleri, kullanılmış ancak iyi durumda olan ürünlere erişim sağlar. Ayrıca, onarıma ihtiyaç duyan eşyalarınızı tamir ederek veya geri dönüştürerek, bu ürünlerin ömrünü uzatabilirsiniz.')
                   
@bot.command()
async def cozum8 (ctx):
    await ctx.send(f'Son olarak, atık yönetimi ve çevre koruma konularında bilgi edinmeye devam etmek önemlidir. Aile üyelerinizi ve çevrenizdeki insanları bu konularda bilinçlendirmek, toplumsal farkındalığı artırabilir. Atık azaltma ve geri dönüşüm konularında eğitimler alabilir, çevre dostu alışkanlıkları yaygınlaştırarak daha büyük bir etki yaratabilirsiniz.')



