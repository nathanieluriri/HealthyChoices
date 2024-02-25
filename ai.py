"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai
# generation_config = {
#   "temperature": 0.9,
#   "top_p": 1,
#   "top_k": 1,
#   "max_output_tokens": 2048,
# }
# Set up the model
genai.configure(api_key="AIzaSyAKNV7BoByxdTHHG3OewIFSBDQhqMK6USs")





# prompt_parts = [
#   "what kind of food will you recommend for a diabetic patient that likes rice",
# ]

# response = genai.generate_text(prompt=prompt_parts[0])
# print(response)

# for model in genai.list_models():
#     print(model)


embedings = genai.generate_embeddings(
    model="models/embedding-gecko-001",
    text="hello everyone how are you doing "
)

# print(embedings['embedding'])





Available_options=[
    '''
1.summer squash salad,Healthy Food,veg,"white balsamic vinegar, lemon juice, lemon rind, red chillies, garlic cloves (crushed), olive oil, summer squash (zucchini), sea salt, black pepper, basil leaves"
2,chicken minced salad,Healthy Food,non-veg,"olive oil, chicken mince, garlic (minced), onion, salt, black pepper, carrot, cabbage, green onions, sweet chilli sauce, peanut butter, ginger, soy sauce, fresh cilantro, red pepper flakes (crushed), tarts"
3,sweet chilli almonds,Snack,veg,"almonds whole, egg white, curry leaves, salt, sugar (fine grain), red chilli powder"
4,tricolour salad,Healthy Food,veg,"vinegar, honey/sugar, soy sauce, salt, garlic cloves (minced), chilli pepper (sliced), green papaya, carrot (peeled), cucumbers, mint leaves, toasted peanuts"
5,christmas cake,Dessert,veg,"christmas dry fruits (pre-soaked), orange zest, lemon zest, jaggery syrup, almond flour, apple, butter (softened), eggs"
6,japanese curry arancini with barley salsa,Japanese,veg,"japanese curry, sticky rice, cheese inside rice, barley salsa, wasabi mayo, red capsicum cube (cut), yellow capsicum cube (cut), green capsicum cube (cut), green chili, barley, butter, white pepper, light soya, salt"
7,chocolate nero cookies,Dessert,veg,"almonds, eggs, granulated sugar, bittersweet chocolate, unsalted butter, flour, baking powder, castor sugar, icing sugar"
8,lamb and chargrilled bell pepper soup,Healthy Food,non-veg,"lamb bones (preferably shank and shoulder), onions, celery, ginger, garlic, carrot, chargrilled red/yellow/green bell peppers (quartered), whole spices mix (black pepper, cinnamon, cardamom, clove, bay leaf), salt, water (warm), oil (sunflower or olive"
9,cream of almond soup,Healthy Food,veg,"vegetable stock, skimmed milk, toasted almonds (powdered), butter, flour, salt and pepper, nutmeg, almond essence, toasted almond flakes"
10,broccoli and almond soup,Healthy Food,veg,"vegetable stock, broccoli, ground almonds (toasted), skimmed milk, salt, freshly ground black pepper"
11,coconut lime quinoa salad,Healthy Food,veg,"uncooked quinoa, water, red onion, cucumber (diced), purple cabbage, avocado (ripened and diced), orange, shelled edamame (defrosted), unsweetened toasted coconut flakes, almonds, few shakes of black pepper, for the dressing:, orange juice, lime (juiced), apple cider vinegar, olive oil"
12,lemon honey glazed sous vide corn on the cob,Snack,non-veg,"young corn on the cob, honey, lemon juice, garlic cloves (smashed), celery stalk, chives, carrot, salt, paprika powder, parsley, plastic bag, food thermometer"
13,watermelon and strawberry smoothie,Healthy Food,veg,"fresh strawberries, honey, low fat yogurt, watermelon, chia seeds"
14,"peach, raspberry and nuts smoothie",Healthy Food,veg,"fresh raspberries, ripe banana, almond, fresh peach slices, low fat yogurt, fresh raspberry, peach fruit slices, almonds"
15,almond and cranberry poha,Indian,veg,"almond flakes, onion, poha, cranberries (frozen/ dried), salt, oil, curry leaves, green chilies, fresh coconut"
16,almond and raw banana galawat,Indian,veg,"almond slivers, raw banana (boiled), almond paste, cooking cream, refined oil, mace powder, cardamom powder , ginger garlic paste, garam masala powder, red chilli powder, salt, tempura batter"


  ''','''
17,baked namakpara with roasted almond dip,Snack,veg,"almonds (crushed), tomato, garlic cloves, basil sprig, lemon, salt, pepper, for namak para:, refined flour, sugar, salt, olive oil, water"
18,grilled almond barfi,Dessert,veg,"khoya, sweetener (optional), almonds (crushed)"
19,baked shankarpali ,Snack,veg,"whole wheat flour (atta), refined flour (maida), garlic cloves (crushed), salt, red chilli powder, chaat masala, cumin powder, tomato puree, ghee"
20,baked multigrain murukku,Snack,veg,"oats, ragi flour (bhakri atta), wheat flour, rice flour, urad dal flour (dry roast and grind the dal to a fine powder), cumin seeds, green chillies, ginger, salt, oil"
21,apple rabdi,Dessert,veg,"apples, milk, sugar, green cardamoms, almonds (blanched), pistachios (blanched)"
22,baked namak para,Snack,veg,"whole wheat flour (atta), refined flour (maida), baking powder, ghee, salt, carom seeds (ajwain)"
23,dates and nuts ladoo,Dessert,veg,"dates (pitted), mixed nuts (almonds, cashews, walnuts, pistachios, peanuts), dessicated coconut (optional)"
24,green lentil dessert fudge,Dessert,veg,"whole moong beans, cow ghee, raisins, whole milk, jaggery (organic), ground cardamom, almonds (halved)"
25,cashew nut cookies,Dessert,veg,"cashew paste, ghee, khaand (a sweetening agent and a healthier substitute of sugar), flax or chia seeds, plain yogurt, baking soda, baking powder, vanilla, oats, organic all-purpose flour"
26,almond pearls,Snack,veg,"toasted almonds, blueberries, oats, corn flakes, olive oil, salt, curry leaves, mustard seeds, cumin seeds, red chilli powder, turmeric powder, black pepper powder, ajwain, lemon juice"
27,hawaiin papaya salad,Healthy Food,veg,"papaya, fresh lime (juiced), watermelon balls or small squares (seedless), fresh pineapple chunks, coconut (unsweetened), vanilla flavoured yogurt (low fat)"
28,vegetable som tam salad,Healthy Food,veg,"raw papaya, carrot, french bean diamond, cherry tomato, garlic, crush mix chilli, somtam dressing, peanuts (crushed), peanuts"
29,spinach and feta crepes,French,veg,"milk (whole fat or skimmed), flour, water, butter, honey, salt, vegetable oil, extra butter (for crisping the crepe), spinach, feta cheese (crumbled), greek yogurt (whisked), honey"
30,couscous with ratatouille - tangy tomato sauce,French,veg,"for the cous cous:, plain couscous, extra virgin olive oil, vegetable stock, herbs (basil, parsley, thyme, cilantro work best), for the ratatouille:, olive oil (regular not extra virgin), red onions, aubergines (cut in to 3 cm cubes), zucchini (cut in to 3 cm cubes), garlic cloves, ground cumin, sweet paprika, tomato paste, salt"
31,baked almond kofta,Snack,veg,"potato (boiled), nutmeg, milk, almonds (crushed), green onions, refined flour, egg, salt, pepper, eggs, refined flour (for rolling), dried breadcrumbs (for rolling)"
32,almond and amaranth ladoo,Dessert,veg,"popped amaranth seeds, jaggery, almonds (slivered, unpeeled)"''',
                   
'''

33,moong dal kiwi coconut soup,Indian,veg,"green gram (dhuli moong dal), kiwis, coconut cream, oil, bay leaves, cumin seeds, coriander seeds, black peppercorns, garlic cloves, medium onion, carrot, turmeric powder, curry powder, salt, fresh coriander sprigs"
34,mixed berry & banana smoothie,Healthy Food,veg,"Frozen mixed berries, ripped banana,fresh orange juice, low fat curd"
35,banana walnut smoothie,Healthy Food,veg,"Low Fat Yogurt, Banana, Walnuts, Seeds (Facseeds and Chia Seeds), Honey"
36,spicy watermelon soup,Healthy Food,veg,"Watermelon, ginger-garlic paste, peppermint, chili flakes, olive oil (to cook)"
37,red rice poha,Indian,veg,"Onion, Pepper, Button Mushroom, Wild Mushroom, White Wine, Tomato, Sage Leaf, Red Poha, Truffle Oil, Rosemary"
38,mixed salad with lotus root,Healthy Food,veg,"Iceberg Lattoos, Lolo Rosso, Endive Lettuce, Red Cabbage, Lotus Root, Kaddu, Yam Beans, Small Onions, Pomegranate, Chalet Oil, Pomelo, Lemongrass Sauce"
39,sweet potato and quinoa bowl,Healthy Food,veg,"Sweet Potato Cubes, Coconut, Onion, Knoia (Ripe), Raisins, Cashew, Pepper Powder, Caen, Cassia, Salt"
40,corn and raw mango salad,Healthy Food,veg,"Corn kernels, onions, green onions, paprika, raw mango (pieces), celery stock (pieces), cherry tomatoes, pineapple (pieces), pasarley, green coriander, badge leaves, black olive, lemon juice, olive Oil, black salt, white pepper powder, taco shell"
''',

'''
41,khichdi,Indian,veg,"Quick cooking oats, peanuts, cumin, turmeric powder, red chilli powder, onion, tomatoes, carrots, green peas, ginger, green chillies, salt, extra virgin olive oil, water, coriander leaves"
42,sugar free modak,Japanese,veg,"seedless dates, almonds, cashew nuts, walnuts, raisins, dry coconut, poppy seeds, ghee"
43,beetroot modak,Japanese,veg,"gram flour (besan), semolina (rava/sooji), beetroot colour or two oven cooked beetroot paste , water, oil (for frying), for sugar syrup:, sugar, water, cardamom powder, lemon juice, cashews (kaju)"
44,andhra pan fried pomfret,Indian,veg,"white pomfret fish, sunflower refined ooil, red chilli powder, salt, turmeric powder, ginger-garlic paste, lemon (juiced), cumin powder, coriander powder, garam masala, green chilli, curry leaves, coriander"
45,ghee roast chicken dosa quesadilla,Mexican,non-veg,"dry red chillies, coriander seeds, cumin seeds, fenugreek seeds, black pepper, clove, garlic, turmeric powder, boneless chicken, curd, lemon (juiced), for cooking chicken:, tamarind pulp, ginger (1 inch), garlic cloves, onion, tomato, ghee, red chilli powder, salt, crushed jaggery, dosa batter (for 4 dosas), processed cheese, ghee or oil (to crisp the dosa), coriander leaves, curry leaves (deep fried), curd, salt, zeera powder, sugar, red chilli powder"
46,steam bunny chicken bao,Japanese,non-veg,"buns, all purpose white flour, dry yeast, sugar, salt, warm water, chicken mince, eggs, soy sauce, sugar, sesame oil, worcestershire sauce, chives, aromat powder"
47,meat lovers pizza,Italian,non-veg,"millet flour, tapioca flour, soy milk, garlic powder, baking powder, salt, tomato sauce, mozzarella cheese, prosciutto, pepperoni, chicken salami, salami milano, rosemary, olive oil"
48,almond and chicken momos (without shell),Chinese,non-veg,"chicken mince, garlic, carrots, spring onion, ginger, soya sauce, oyster sauce, sesame oil, pepper powder, egg, almonds (blanched), oil (for greasing)"
49,christmas tree pizza,Italian,veg,"pizza dough (2 boules), red pepper, red onion, basil pesto (purchased, homemade or vegan pesto), mozzarella cheese, kosher salt"
50,french pork chop,French,veg,"pork chop, pink pepper corn, green pepper corn, aromatic sauce, salt, black pepper, salted butter, refined oil, red cabbage, bell pepper chop, apricot, onion, red wine, ancho chilli, cayenne pepper, microgreen"
51,christmas chocolate fudge cookies,Dessert,veg,"unsalted butter, brown sugar, chocolate, chocolate chips, eggs, flour, cocoa powder, baking powder"
52,chicken parmigiana with tomato sauce,Italian,non-veg,"for chicken parmigiana:, chicken breast, egg whole frozen, flour, planko bread crumbs, fresh italian parsley, vegetable oil, solid butter unsalted, tomato sauce, mozzarella cheese, italian parmesan cheese, thyme, for pepperonata:, red pepper, green pepper, yellow pepper, red onion, fresh tomato, butternut squash, garlic, pure olive oil, vegetable oil, black pepper corn (crushed), salt, parsley, for garnishing:, parsley sprig, spinach"
53,chocolate appe,Snack,veg,"rice, coconut, baking powder, vanilla extract, cinnamon powder, brown sugar, unsweetened cocoa powder, salt, chocolate chips, butter"
54,sous-vide salmon tikka,French,non-veg,"norwegian salmon, black garlic pickle, butter, butchery bag, smoked yogurt, home made prawn crisp, edible flower, salt"
55,filo pizza,Italian,veg,"filo pastry, himalayan salt, black pepper, salted butter, tomato sauce, broccoli, button mushroom, green zucchini, yellow zucchini, capsicum yellow, capsicum green, capsicum red, pizza spice mix, mozzarella cheese"
''',
'''
56,chocolate samosa,Snack,veg,"refined flour, desi ghee, black cardamom seeds, chocolate block, almonds, cashew nuts, pistachio, sugar, garam masala powder, oil"
57,fish with jamun sauce,Indian,non-veg,"jamun, sugar, chilli, garlic cloves (minced), cumin (powdered), fish fillet (pomfret (or any white fish), semolina, salt, wilted spinach"
58,dahi lasooni chicken,Indian,non-veg,"chicken (boneless, cube size), chesse, garlic, ginger garlic paste, coriander, green chilli paste, cream (fresh), curd, kaju paste, salt, black salt , garam masala, chaat masala, butter"
59,pesto fish kebabs,Indian,non-veg,"King fish cut into one inch pieces, paprika cut into one inch pieces, bezel pasto, white wine vinegar, salt, cooking spray"
60,caramelized sesame smoked almonds,Snack,veg,"red lentils or masoor dal (half-boiled), potato (grated), carrot, french beans, bread slices, ground chickpea flour (sattu), green chillies, ginger, onions, garlic (minced), salt, sugar, chaat masala, red chilli powder, garam masala, corn flour, besan, bread crumbs for crunchyness, coriander, refined oil (for fryingp)"
61,crunchy vegetable dal sattu croquettes,Italian,veg,"red lentils or masoor dal (half-boiled), potato (grated), carrot, french beans, bread slices, ground chickpea flour (sattu), green chillies, ginger, onions, garlic (minced), salt, sugar, chaat masala, red chilli powder, garam masala, corn flour, besan, bread crumbs for crunchyness, coriander, refined oil (for fryingp)"
''',

'''
62,active charcoal modak,Japanese,veg,"for modak:, gram flour (besan), semolina (rava/suji), active charcoal, water, oil (for frying), sugar, water, cardamom powder, lemon juice, cashews (kaju)"
63,flax seed and beetroot modak,Japanese,veg,"rice flour, salt, oil (for greasing), beetroot puree, tossed flax seeds (for topping), fresh coconut, jaggery, poppy seeds, green cardamom powder, nutmeg powder"
64,chocolate prunes gujiyas,Japanese,veg,"for gujiya pastry:, refined flour, ghee, water, salt, for gujiya stuffing:, dark chocolate, prunes, mawa, sugar, cardamom"
65,almond  white chocolate gujiya,Japanese,veg,"all-purpose flour, clarified butter (ghee), water, white chocolate, dessicated coconut, green cardamom powder, almond, jaggery"
66,betel nut popsicle,Dessert,veg,"full cream milk, cream, mascarpone, sugar, paan (crushed), cookie crumble, dark chocolate (melted), caramel sauce"
67,clotted cottage cheese croquettes,Italian,veg,"black pepper, black salt, bread crumb, corn flour, refined oil, jalapeno, jeera powder, maida, cottage cheese, parsley, salt, for thousand island dressing:, mayonnaise, tomato ketchup, minced garlic, celery, black pepper"
68,gajar tart,French,veg,"white butter, breakfast sugar, milk full fat, refined flour, winter carrots, ghee, sugar, khoya, cardamom powder, cashew nuts (crushed), almonds (crushed), full fat milk, full fat milk, grain sugar, green cardamom powder"
69,banana and maple ice lollies,Dessert,veg,"Banana, Greek yogurt, heavy cream, pure maple syrup, coconut"
70,shepherds salad (tamatar-kheera salaad),Healthy Food,veg,"1 cucumber peeled and chopped, onion, tomato, green chillies, garlic buds, pasarley, olive oil, lemon juice, salt and pepper"
71,carrot ginger soup,Healthy Food,veg,"Carrots, Olive Oil, Salt, Vegetable Stock, Ginger, Thyme, Onion, Garlic Buds, Pepper (Freshly Picked)"
72,dark night,Beverage,veg,"whisky, honey, cinnamon, star anise, cloves, green apple"
73,hot chocolate,Beverage,veg,"milk, chocolate, cocoa powder, powdered sugar, cinnamon, vanilla"
74,slow cooked spiced sangria,Mexican,veg,"red wine (merlot / zinfandel), apple cider, honey, orange (zested and juiced), cloves (whole), green cardamom, cinnamon sticks, anise (whole), brandy"
75,detox haldi tea,Beverage,veg,"haldi, ginger, black pepper, honey, water"
76,holi special ice tea thandai,Beverage,veg,"ground white pepper (kali mirch), assam tea bags, almonds (badam) - coarsley crushed, poppy seeds (khus-khus), fennel seeds (saunf) (crushed coarsely), cardamom (elaichi) powder, ground sugar, saffron (kesar) strands"
''',
'''
77,grilled lemon margarita,Beverage,veg,"vanilla infused tequila, vanilla liqueur, lemon juice, lemon, lemon"
78,spanish artichoke and spinach dip,Mexican,veg,"spinach, onion, cream, garlic, nutmeg, salt, lime juice, artichoke hearts (cubed), polenta, refined flour, salt, water, butter, flour, salt, pepper (freshly ground)"
79,beetroot and green apple soup,Healthy Food,veg,"beetroots, green apple, onion, olive oil, salt, black peppercorns (crushed), butter, vegetable stock, mixed dried herbs, fresh cream, lemon juice, parsley sprigs, red chilli flakes, soup sticks as required"
80,baba budan no. 7,Beverage,veg,"rum, espresso, sugar syrup/gur (jaggery) syrup, green cardamom pod,"
81,fruit infused tea,Beverage,veg,"chamomile tea bags, orange, berries, blueberries, ginger, mint leaves, boiling water"
82,soya milk,Beverage,veg,"Soybean, hot water"
83,spiced coffee,Beverage,veg,"Freshly ground coffee, cardamom powder, ginger, milk, sugar, cream, chocolate"
84,filter coffee,Beverage,veg,"Coffee powder, water, milk, sugar"
85,garlic and pinenut soup with burnt butter essence,French,veg,"garlic cloves, almonds (whole), parsley, bayleaf, chicken broth, nutmeg, egg yolk, heavy cream, white bread slices, butter, salt, pepper, white wine"
86,roast turkey with cranberry sauce,Healthy Food,non-veg,"whole turkey, butter, onion, celery, crumbled sage and thyme , salt and pepper, garlic minced, balsamic vinegar, sugar, cranberry"
87,roasted spring chicken with root veggies,Healthy Food,non-veg,"whole chicken, thyme, garlic, lemon, orange, salt, black pepper, butter (to rub), extra olive oil, carrot, turnip, beetroot, chipotle powder, parsley"
''',

'''
88,peri peri chicken satay,Snack,non-veg,"boneless skinless chicken thigh (trimmed), salt and pepper, yogurt, chilli powder, ginger garlic paste, coriander leaves, oil to fry, peri peri sauce, potato fries"
89,chicken popcorn,Chinese,non-veg,"chicken (boneless), corn flour or all purpose flour, egg, bread crumbs, salt, ginger garlic paste, black pepper, onion powder (optional), red chilli powder or paprika or cayenne pepper, oil for deep frying"
90,half roast chicken,Healthy Food,non-veg,"cooking oil, whole chicken (skin on- rinsed and dressed), onions (quartered- skin on), garlic (halved - skin on), carrots (roughly quartered), celery , thyme, dunkleweizen (pour into a glass and keep open at room temperature for an hour or two to make flat), chicken stock, butter, sea salt"
91,chicken biryani,Indian,non-veg,"malabar peppercorn, cinnamon stick, green cardamom pods, star anise, cloves, fennel seeds, vermicelli, desi ghee, shahi jeera, bay leaves, green chilli, mint leaves, onion, saffron, garlic paste, salt, chicken (dark meat), ginger paste, turmeric powder, coriander powder, red chilli powder, roma tomatoes (de-seedeed), water"
92,chicken farcha,Indian,non-veg,"boneless chicken thigh (without skin), lemon juice, garlic paste, ginger paste, red chilli powder, coriander powder, garam masala, black pepper (crushed), salt, bread crumbs / semolina, eggs, red chilli powder, oil"
93,buldak (hot and spicy chicken),Japanese,non-veg,"chicken drum sticks/ chicken breast, soy sauce, sugar, traditional corn syrup (substitution honey), cheong ju (clear rice wine similar to japanese sake), green onion, black pepper, olive oil, sesame seeds (optional), for marinating sauce:, gochugaru (red chili pepper flakes), alapenos, korean pear (substitution asian pear), onion, garlic, soy sauce, spicy yellow mustard, sesame oil, sugar, mul yut (substitution honey)"
94,chicken sukka,Indian,non-veg,"chicken (small pieces), onion (thin slices), cardamom, salt, oil, coriander, cumin, mustard, pepper, cloves, cinnamon, bedki chillies, kashmiri chilies, turmeric, onion, garlic, ginger, salt"
95,steamed chicken roulade,French,non-veg,"lamb mince, garlic , salt, paprika powder, pomodaro tomatoes, olive oil, celery, shallots, carrot, black pepper, bay leaf, yellow chilli powder, cilantro, chicken thigh, salt, white pepper powder, garlic paste, white wine vinegar, olive oil, yellow chilli powder, refined oil, fenugreek seeds, white pepper powder, garlic, fenugreek leaves, onion, broken cashew, salt, fresh cream, kasoori methi"
96,methi chicken masala,Indian,non-veg,"boneless chicken, lemon juice, red chilli powder, salt, ginger garlic paste, curd, red chilli powder, salt, coriander powder, oil, onion, oil, bay leaf, green cardamom, black cardamom, cinnamon, ginger garlic paste, tomato, kasoori methi, green chilli, water"
97,restaurant style fried chicken,Chinese,non-veg,"egg, salt, white pepper, maida, salt, red chilli powder, garlic powder, ginger powder, onion powder, oregano, chillil flakes, white pepper, basil, chicken drumsticks, salt, white pepper, bread crumbs (as required)"
98,chicken potli,Chinese,non-veg,"chicken, onion, green chilli, garlic, ginger, salt, aromatic powder, soya sauce, oyster sauce, spring onion, filo sheets"
99,spicy chicken masala,Indian,non-veg,"mustard oil, curry leaves, kalonjee, saunf, garlic, onion, tomatoes, ginger, green chillies, boneless chicken, salt, tomato puree, red chilli powder, cumin powder, black salt, peppercorn (crushed), water, mint, coriander"
100,spicy chicken curry,Indian,non-veg,"oil, ghee, onion paste, garlic paste, ginger paste, turmeric powder, salt, tomato puree, coriander powder, red chilli powder, cumin powder, garam masala, chicken leg pieces, coriander leaves, water"
''',
'''
101,crispy herb chicken,Italian,non-veg,"fresh breadcrumbs, parmesan cheese, lemon rind, fresh parsley leaves, garlic powder, plain flour, egg, milk, chicken breast supremes, vegetable oil, mayonnaise, sour cream, fresh chives (dried if fresh not available), fresh parsley (dried if fresh not available), garlic, red onion (optional), ground black pepper, salt"
102,dahi chicken,Indian,non-veg,"dahi, cumin powder, garlic paste, garam masala, turmeric powder, red chilli powder, salt, boneless chicken, oil, green chilli, onion, tomato"
103,amritsari chicken masala,Indian,non-veg,"chicken, ginger garlic paste, curd, lemon juice, vinegar, coriander powder, cumin powder, red chilli powder, salt, onion, butter, red chilli powder, coriander powder, cumin powder, ginger, water, salt, green chilli, tomatoes, sugar, butter , cream"
104,chilli chicken,Chinese,non-veg,"boneless chicken, salt, cornflour, black pepper, egg, soy sauce, red chilli sauce, garlic, green chillies, green chilli sauce, vinegar, onion, capsicum, black pepper, salt"
105,chicken tenders,Snack,non-veg,"chicken breast (cut into strips), salt, garlic paste, ginger paste, green chilli paste, oats, refined flour, salt, freshly ground black pepper, fried mixed herbs (italian herb), garlic powder"
106,chicken nimbu dhaniya shorba,Beverage,non-veg,"water, chicken (diced)), ginger garlic paste, coriander, lemon, cream, butter, turmeric powder, green chilli paste, cornflour, salt"
107,garlic soya chicken,Healthy Food,non-veg,"chicken thigh/breast (cut crosswise into 1/2-inch-thin strips), sesame oil (toasted), white pepper (finely ground), ginger juice, peanut oil or vegetable oil (divided), garlic cloves (minced), ginger, red chilli flakes, red onion , snow peas (trimmed), red bell pepper (cut into thin strips), rice vinegar, soy sauce, dark soy sauce, chinese rice wine, brown sugar, cornflour"
108,cauliflower and chicken biryani,Indian,non-veg,"boneless chicken, biryani masala, yogurt, onions, coconut oil, cauliflower, coconut (diced), onion (diced), peppercorns, cardamoms, cumin seeds, bay leaves, cinnamon, cloves, coconut oil, garam masala, dry chilli flakes, turmeric powder, black peppercorns, cardamom, cinnamon, garlic (crushed), tomato puree, green chillies, fresh ginger (peeled), dry red chilli, salt"
109,chicken quinoa biryani,Healthy Food,non-veg,"onions, tomato, green chillies(slit open), ginger garlic paste, mint leaves, coriander leaves/cilantro, fresh yogurt/curd(beaten), turmeric powder, chilli powder, salt, chicken (cut into pieces), garam masala powder, ginger garlic paste, yogurt/curd, chilli powder, coriander powder, salt, oil, cloves, bay leaf , cardamom"
110,chicken and mushroom lasagna,Italian,non-veg,"chicken, salt, crush black pepper, garlic cloves (minced), olive oil, fresh thyme, button mushroom, onion, low fat milk, basil, basil-tomato sauce"
111,plum and cherry roasted chicken,Healthy Food,non-veg,"carrot (finely diced), onion (finely diced), celery (finely diced), fresh thyme sprigs, whole free range chicken , pepper (freshly ground), parsley stems, celery leaves, lemon slices (1/8 inch thick), onion, carrot, fresh lemon juice, chicken stock/broth, plums (cut), fresh cherries"
112,chicken roulade,French,non-veg,"chicken breasts, olives, jalapenos, bell peppers(all 3), thyme dried, white wine, salt, black pepper (crushed to taste), egg, olive oil, mozerella cheese, processed cheese"
113,sticky rum chicken wings,Snack,non-veg,"chicken wings without skin, hung curd, chilli powder, sweet paprika powder, english mustard paste, garlic paste, salt, garlic, rum, bbq sauce"
114,chicken dragon,Chinese,non-veg,"Chicken (boneless and cut into small pieces), eggs (lightly whipped), maida, garlic paste, ginger paste, salt, water, oil"
115,chicken palwal,Indian,non-veg,"Chicken, Onion, Tomato, Green Chilli, Cumin Powder, Coriander Powder, Green Coriander, Curd, Ginger Garlic, Red Chilli Powder, Salt, Oil"
''',

'''
116,pan seared thigh of chicken,Mexican,non-veg,"Chicken Thai, Salt, Pepper, Lemon, Fresh Thyme, Barley, Brockley, Mushroom, Extra Virgin Olive Oil, Cherry Tomato"
117,chicken in mahalak sauce,Indian,non-veg,"Salt, sugar, seasonings, oil, corn flour, chicken leg, fresh chilli, garlic, ginger, onion, red chili paste, tomato catchup, paprika, yellow capsicum, vegetable stock"
118,grilled kasundi honey chicken with sweet potato mash,Indian,non-veg,"Chicken breast, kasundi (Bengali mustard sauce), sweet potato, red and yellow capsicum, broccoli, garlic buds, refined oil, salt, butter, cream, green onion, honey, ginger and garlic paste"
119,chicken dong style,Chinese,non-veg,"Oil, chicken breast, garlic, ginger, tomato catchup, oyster sauce, shitake mushrooms, bomb shoots (boiled), salt, sugar, broth powder, shocking wine, potato starch, sesame oil, green onions"
120,microwave tandoori chicken,Indian,non-veg,"Chicken (sliced), garlic paste, ginger paste, Hung curd, salt, garam masala, coriander powder, pepper powder, cream, oil, for garnishing:, lemon pieces, onion rings"
121,methi malai cranberry chicken,Indian,non-veg,"Chicken (sliced ??into large pieces), salt, cranberry puree, red chilli powder, garam masala, coriander powder, cumin powder, chaat masala, corn flour, fenugreek leaves, gram flour, ginger, garlic, cream, Greek yogurt, butter"
122,southern fried chicken tenders,Snack,non-veg,"Chicken breast (cut 20 strips, 20 grams), all purpose flour, salt, hot red chillies, eggs, bread crumbles, white cabbage slaw, pasarley sprig, honey-mustard dip, green bell pepper"
123,thai style chicken tikka,Thai,non-veg,"Chicken Thais, Thai Ginger, Lemon Leaves, Lemongrass, Coconut Milk Powder, Refined Oil, Red Curry Paste, Peanut Butter, Bezel Leaves, Lotus Stem, Yellow Butter, Chaat Masala"
124,chicken gilafi kebab,Indian,non-veg,"Chicken Mince, Onion, Tomato, Green Capsicum, Green Coriander, Green Chilli, Salt, Oil, Cashew, Almond, Mint, Red Chilli Powder, Ginger Garlic Paste, Cumin Powder, Lemon Juice, Fresh Cream, Kewda Water"
125,cheese chicken kebabs,Indian,non-veg,"Chicken Thais, Garlic Paste, Garlic Paste, Yellow Chilli Powder, Cheese, Curd, Gram Flour, Green Cardamom Powder, Yellow Chilli Powder, Mace Powder, Nutmeg Powder, Rock Salt, Green Coriander, Oil"
126,andhra crab meat masala,Indian,non-veg,"processed crab meat, refined oil, curry leaves, garlic, green chilli, onion, ginger-garlic paste, coriander, coriander powder, cumin powder, turmeric powder, garam masala powder, kashmiri chilli powder, salt, lemon, chop masala, tomato"
127,cajun spiced turkey wrapped with bacon,Mexican,non-veg,"turkey breast, cajun spice, spinach leaves (cooked and drained), garlic pods, salted butter, feta cheese, bacon strips, ground black pepper, for cajun spice:, onion powder, garlic powder, seasoning salt, paprika, ground black pepper, cayenne pepper, oregano, thyme, red pepper flakes (if you like it spicy))"
128,thai lamb balls,Thai,non-veg,"lamb (minced), couscous, scallion, garlic, egg, parsley, olive oil, mint, ao nori herb, salt, five spice, cinnamon powder"
129,oyster lamb,Thai,non-veg,"vegetable oil, garlic, ginger, lamb, stock, oyster sauce, dry sherry, sugar, celery, salt, bokchoy, shitake mushroom"
130,chicken shami kebab,Indian,non-veg,"oil, cumin seeds, cloves, black peppercorns, cinnamon, coriander seeds, ajwain, red chilli whole, chilli flakes, boneless chicken, salt, water, ginger, green chilli, garlic, coriander leaves , mint leaves , egg"
131,balti meat,Mexican,non-veg,"refined oil, black cardamoms, green cardamoms, mace, clove, cinnamon stick, black pepper corn, ginger garlic paste, ginger, green chilies, mutton curry cut, brown onion paste, salt, kashmiri red chili powder, tomato puree, garam masala powder, coriander powder, cumin powder"
132,coffee marinated mutton chops,Thai,non-veg,"mutton chops, espresso, honey, balsamic vinegar, rosemary, pink peppercorns (crushed), olive oil, salt"
133,sali boti (parsi meat dish),Indian,non-veg,"mutton (wash and cut into very small cubes), ghee or oil, tomatoes, onions, green chillies, coriander leaves, chilli powder, turmeric powder, ginger-garlic paste, water, vinegar, jaggery, salt, potatoes, oil"
134,braised lamb shanks,Thai,non-veg,"Lang Shanks, Olive Oil, Onion, Carrots, Celery Stick, Garlic, White Wine, Lamb Stock, White Wine, Rosemary, Tomata Puree"
135,bengali lamb curry,Indian,non-veg,"Lamb pieces, yogurt, turmeric powder, castor sugar, red chili powder, mustard oil, onion, ginger paste, garlic paste, green chillies, mustard seeds, almonds"
136,malabari fish curry,Indian,non-veg,"sear fish, coconut, ginger, pureed tamarind, salt, powdered turmeric, green chillies, red chilli powder, shallots"
''',
'''
137,japanese fish stew,Japanese,non-veg,"sole fillet (you can also do 2/3 types of fish), large shrimps (optional), potatoes (peeled), onions (cut into slices), garlic cloves, red capsicum (can use green also), parsley or coriander (choose the herb that most suits your taste buds), few dashes of hot sauce, paprika, olive oil, white wine, rock salt"
138,malabar fish curry,Indian,non-veg,"whole coriander seeds, whole red chilli, coconut oil, mustard seeds, onion, curry leaf, coconut milk, tamarind pulp, coriander, seabass fish curry cuts"
139,surmai curry with lobster butter rice,Thai,veg,"tamarind, red chilli powder, turmeric powder, salt, fresh coconut, onion, garlic cloves, coriander seeds, fenugreek seeds, red chilli powder, turmeric powder, tamarind (lemon sized), butter, lobster (de-shell and devein and make a small cube), salt and lime, surmai"
140,seared salmon in tabasco butter,Thai,non-veg,"butter, tabasco, chives, salt, salmon fillet, olive oil, sea salt"
141,"risotto lobster with parmesan egg pancake, confit tomatoes and coral tuille",Italian,non-veg,"lobster shell, carrot, leeks, garlic cloves, tomato paste, bay leaf, peppercorn, water, lobster meat, arborio rice, onion, leeks, lobster stock, parmesan cheese, cream, salt, olive oil, egg, parmesan, flour, milk, parsley, salt, cherry tomatoes, garlic pods, olive oil, water, oil, flour, salt"
142,fish skewers with coriander and red wine vinegar dressing,Thai,non-veg,"sea bass fillets, olive oil (for grilling), red wine vinegar, sugar, extra virgin olive oil, garlic clove, coriander, bamboo skewers"
143,seafood rock filler,French,veg,"baked tart of mixed sea food served with phyllo fruit bowl, savory tart shell (semi baked), mixed sea food, mornay sauce, assorted herb and seasoning, phyllo pastry, assorted seasonal fruit"
144,shrimp & cilantro ceviche,French,veg,"prawns, gherkin, onion, cilantro, mix bell pepper, tiger milk, sweet corn, sea salt, black pepper, green lemon juice, cherry tomato, edible flower, coriander stems, celery stalks, garlic, ginger, red onion, lemon juice, sea salt, black pepper"
145,saewoo bokumbop (shrimp fried rice),Japanese,veg,"cooked rice, shrimp (de-veined, onion, cooked green peas, green onion, egg (scrambled), vegetable oil/butter, soy sauce, sesame oil, salt, pepper"
146,thai prawn curry & baked rice ,Thai,veg,"jeera whole, coriander seeds, kashmiri chilly, garlic, ginger, green chillies, kokum, coconut, onion, tomatoes, coriander, prawns, salt, turmeric powder, garlic paste, asafoetida, refined oil, ginger paste, goan rice, coconut milk, green chillies, fresh coconut, hing, refined oil, coriander leaves, basmati rice, coconut milk, green chillies, coconut milk, coconut, salt, green chillies, curry leaf, lecite"
147,bihari fish curry,Indian,non-veg,"rohu fish, salt, turmeric powder, chilli powder, oil, garlic , green chillies, mustard seeds, black peppercorns, cumin seeds, whole red chillies, fenugreek seeds, tomatoes, mustard oil, bay leaves, water, garam masala, coriander leaves"
148,curry fish fingers,Thai,non-veg,"river sole fish (cut in thin strips), garlic paste, salt , lime juice, beer, flour, cornflour, white pepper, eggs, mustard"
149,prawn and litchi salad,Healthy Food,veg,"prawns (shelled and cleaned), spring onions, mango flesh, litchis (deseeded), chilli flakes, lemon (for lemon juice), olive oil, peanuts (to garnish), salt"
150,kerala fish curry,Indian,non-veg,"white fish (cut into cubes), onion, tomato, garlic cloves, fresh green chillies (deseeded), oil, fresh coconut paste, red chilli paste, coriander powder, turmeric powder, salt, whole dry red chillies, black mustard seeds, curry leaves, tamarind extract, water"
''',

'''
151,fish andlouse,French,non-veg,"white wine and water mix to cover, onion, salt, bay leaf, black pepper corns, olive oil, onion, garlic, tomatoes (peeled and seeded), basil leaves, spring fresh thyme - optional 1 bay leaf, salt and pepper, olive oil, wine vinegar, prepared mustard, salt and pepper, assorted garden herbs ( parsley, basil etc."
152,prawn fried rice,Thai,veg,"Oil, Bacon, Prawns, Chicken, Carrots, Garlic Buds, Ginger, Spring Onion, Sweet Chili Sauce, Soy Sauce, Salt, Pepper, Sweet Corn, Vinegar, Baked Rice, Green Coriander"
153,damdama fish curry,Indian,non-veg,"Fish, onion, tomato, reshagi red chilli powder, cumin powder, coriander powder, coriander, cumin, salt, oil"
154,fish with white sauce,Italian,non-veg,"Fillet fish, oil, milk, flour, butter, salt, ground black pepper"
155,chilli fish,Chinese,non-veg,"For fish pieces (Boneless), Flour, Cornflour, Baking Powder, Soy Sauce, Celery, Pepper, Salt, Oil, Green Onion, Sauce:, Ginger, Garlic, Green Chili, Soy Sauce, Tomato Sauce, Chili Sauce, Cornflour"
156,fish ambultiyal,Indian,non-veg,"Tuna, onion, fenugreek, whole chilli, pandan leaf, salt, water, cardamom, cinnamon, coriander powder, black pepper, red chilli, curry powder, garlic (crushed), chili flakes, gorca, salt"
157,chettinad fish fry,Indian,non-veg,"Surmai fish, oil, garlic buds, ginger (mash), cumin, fennel, whole coriander, black pepper, mustard seeds, curry leaves, salt, oil, water, tomatoes, red pepper powder, turmeric powder, tamarind pulp, cornflour, lemon pieces of"
158,fish moilee,Indian,non-veg,"Basa fish, onion, ginger, garlic buds, green chillies, turmeric, red chilli powder, coriander powder, lemon juice, curry leaves, refined oil, refined oil, mustard seeds, black pepper, fennel, green cardamom, coconut milk, Cherry tomatoes"
159,batter fish,Mexican,non-veg,"Fresh fish pieces (river sol or sea bass), maida, passerley, oil, baking powder, maida, egg (optional), soda water, salt and pepper"
160,fish salan,Mexican,non-veg,"King fish, ripe tomatoes, desi ghee, ginger-garlic paste, onion, turmeric powder, red chilli powder, black pepper powder, garam masala, ginger, turmeric powder, fennel powder, refined oil, salt, water"
161,spanish fish fry,Mexican,non-veg,"Sol fish, tomato, onion, lemon juice, olive oil, ginger and garlic paste, bay leaves, cinnamon stick, green chillies, vinegar, salt, water"
162,prawn potato soup,Thai,veg,"Onion, potato, prawns, eggs, milk, butter, coriander, salt, water"
163,red rice vermicelli kheer,Indian,veg,"red rice vermicelli / broken sooji / semolina vermicelli, butter, almonds, whole milk, cardamom powder, saffron strands / thread, sugar"
164,green cucumber shots,Healthy Food,veg,"english cucumbers, garlic cloves (smashed), romaine lettuce, basil, parsley, cilantro, big lemon, sea salt, olive oil"
165,thai pineapple rice,Thai,veg,"rice, onion, thai ginger , fresh turmeric, curry leaf, lemon grass, coconut milk, salt, hot curry powder, pineapple chunks, oil, water, turmeric powder, fresh pineapple"
166,green asparagus risotto,Italian,veg,"carnaroli rice, vegetable broth, butter, extra virgin olive oil, parmigiano cheese, onion (minced), white wine, salt & pepper"
167,veg fried rice,Chinese,veg,"oil, ginger-garlic paste, spring onion, carrot, cabbage, capsicum, salt, soy sauce, vinegar, rice"
''',

'''
168,egg and garlic fried rice,Chinese,non-veg,"oil, garlic, spring onion , ginger, red chilli , egg, cooked rice, salt, black pepper powder, soya sauce"
169,curd rice,Indian,veg,"rice, water, curd, milk, carrot, green chilli, ginger, salt, coriander leaves, oil, mustard seeds, chana dal, urad dal, curry leaves, red chilli, hing"
170,fried rice with soya chunks,Chinese,veg,"basmati rice, carrot, capsicum, beans, green peas, ginger, garlic, green chillies, bay leaf, cinnamon sticks, green cardamoms, clove, soya chunks, salt,"
171,corn pulao,Indian,veg,"basmati rice, american corn kernels, olive oil, onion, ginger garlic paste, salt, green chillies, cumin seed, bay leaf, pepper corn, cloves, hot water, coriander leaves, lime juice, bell pepper (saut?ed and diced), coconut"
172,zucchini methi pulao,Indian,veg,"zucchini, basmati rice, fenugreek (methi), clarified butter (desi ghee), clarified butter (desi ghee), cumin seeds (jeera), asafoetida (heeng), green chilles, ginger, salt"
173,lemon rice,Indian,veg,"cooked basmati rice, oil, asafoetida (heeng), mustard seeds (sarson), curry leaves (kadhi patta), whole red chilli (sabut laal mirch), turmeric powder(haldi), salt, lemon juice, peanuts, urad dal, chana dal, ginger"
174,kale channe ki biryani,Indian,veg,"black gram (kala chana), basmati rice (soaked for 2 hours), cinnamon, green cardamoms, cloves, ghee, black cardamoms, black peppercorns, bay leaves, onions, green chillies (slit), ginger-garlic paste, coriander powder, turmeric powder, yogurt, fresh mint leaves, fresh coriander leaves, garam masala powder, red chilli powder, salt, cashew nuts, almonds, milk, fresh cream, saffron, ginger, screw pine essence (kewra), browned onions, whole wheat flour dough"
175,chicken paella,Mexican,non-veg,"chicken, oil, salt and pepper, paprika powder, chilli flakes, garlic paste, onions, bell peppers, rice, vegetable stock, saffron, peas, olives, parsley, white wine"
176,thai fish curry,Thai,non-veg,"fish (cubed), thai green curry paste, oil, onions, garlic, ginger/galangal, coconut milk, coriander, lemon juice, palm sugar, basil leaves, salt & pepper"
177,vegetable pulao,Indian,veg,"water, basmati rice, ghee, paneer (cooked), carrot, beans, peas, elaichi, cardamoms, cinnamon, bay leaves, cumin seeds, chilli powder, turmeric, salt, coriander leaves"
178,oats shallots pulao,Healthy Food,veg,"Rice, Green Coriander, Green Chillies, Onion, Cinnamon, Cardamom, Cloves, Red Chilli Powder, Salt, Garlic Flakes, Ginger, Chalet, Olive Oil"
179,shiitake fried rice with water chestnuts,Chinese,veg,"Shitake Mushrooms, Vegetable Oil, Garlic Buds, Green Chillies, Water chestnuts, Onions, Leaks, Celery, Ginger, Sesame Oil, Rice Baked, White Chillies, Salt, Rice Wine Vinegar, Green Onions, Small Bunch Pasarley, Sesame Oil"
180,lotus leaf wrapped fried rice,Chinese,veg,"Jasmine Rice (Baked), Edamame Beans, Mock Meat, Shitake Mushroom, Spring Onion, Dark Soy Sauce, Sunflower Oil, Salt"
''',
'''
181,vegetable biryani,Indian,veg,"Cumin, Onion, Ginger Garlic, Mix Vegetable, Coriander Powder, Garam Masala, Turmeric Powder, Salt, Red Chilli Powder, Green Chillies, Lemon Juice, Steamed Rice, Green Coriander"
182,avial with red rice,Indian,veg,"Red rice, water, potatoes, carrots, raw banana, drumstick, small raw mango, sour curd, bean stick, onion, salt, turmeric, water, coconut oil, green chillies, mustard seeds (crushed)"
183,rice in lamb stock,Thai,non-veg,"Rice, desi ghee, big cardamom, bay leaf, cinnamon stick, fennel, onion, lamb bonz, royal cumin, cashew, cream, green cardamom powder, salt, water"
184,vegetable bruschetta,Italian,veg,"baguette (grilled slices), black olive tapenade, artichoke hearts, lettuce arugula (trummed), tomato confit, fresh basil leaves, mint leaves, zucchini, goat cheese, parmesan cheese shavings, mozzarella buffalo cheese"
185,red wine braised mushroom flatbread,Italian,veg,"olive oil, fresh buffalo mozzarella cheese, canned pelati tomatoes (cooked), pizza/flatbread base, mushrooms, red wine, parsley, garlic cloves (halved), salt"
186,strawberry & pistachio breton tart,Dessert,veg,"plain flour, baking powder, sea salt, unsalted butter, egg yoks, castor sugar, double cream, yolk, sugar, gelatine, butter, pistachio paste, strawberry"
187,tricolour pizza,Italian,veg,"pizza base , pizza sauce, mozzarella cheese, black olive, green capsicum, carrots, olive oil"
188,instant rava dosa,Indian,veg,"rava/suji/semolina, rice flour, all purpose flour, fresh coconut (pieces), jeera, green chilli, dhaniya, onion (diced), salt, water, oil, ghee/clarified butter"
189,easy bread poha,Indian,veg,"oil, hing, mustard seeds, curry leaves, whole red chillies, cookes peas, peanuts, turmeric powder, salt, bread, green chillies, lemon juice, coriander leaves, dessicated coconut"
190,bread chana basket,Indian,veg,"bread (white/brown), butter, for chana chaat:, chana, onion, tomatoes, cumin seeds, ginger garlic paste, chilli powder, chana masala, turmeric powder , oil, salt"
191,spaghetti with clams & crispy bread crumbs,Italian,veg,"panko, 1/4 cup plus 1 tablespoon extra-virgin olive oil, plus more for drizzling, kosher salt, freshly ground pepper, garlic cloves, manila clams or cockles, scrubbed, dry white wine, spaghetti, lemon zest, lemon juice, mullet bottarga (optional; see note), red pepper, thyme, rosemary, parsley"
192,kasha bread,French,veg,"kasha, boiling water, buckwheat flour, all-purpose gluten free flour, brown sugar, baking powder, baking soda, xanthum gum, salt, buttermilk, cream, egg, oil, walnuts"
193,egg paratha,Indian,non-veg,"whole wheat flour, salt, oil, eggs, onions, green chilli, coriander leaves, garam masala"
194,egg and cheddar cheese sandwich,Mexican,non-veg,"egg, salt, pepper, ham slices, basil leaves"
195,egg in a blanket,French,non-veg,"eggs, brown bread slices, butter, chilli flakes, oregano, salt"
196,bread dahi vada,Indian,veg,"bread slices, curd, oil, salt and black pepper , red chilli powder, aamchoor powder, mint leaves, zeera powder, anardana"
197,cheese and avocado parantha,Mexican,veg,"Wheat flour, Kasuri methi, water, olive oil, avocado, mozzarella cheese, pizza tasting, ghee, salt"
''',
'''
198,bread with tomatoes and olives,Italian,veg,"French Bread Loaf, Tomato, Extra Virgin Olive Oil, Salt, Black Pepper, Passerley, Stuffed Green Olive"
199,lemon poppy seed cake,Dessert,veg,"plain flour, baking powder, salt, castor sugar, baking soda, eggs, butter, vanilla essence, lemon juice, poppy seed, lemon peel, to serve:, lemon syrup, whip cream, fresh berry"
200,chocolate kaju katli,Dessert,veg,"cashew nuts, sugar, water, milk chocolate or dark chocolate"
201,mix fruit laccha rabri tortilla crunch,Mexican,veg,"milk, sugar, cardamom powder, saffron, almonds and pistachios, grapes, apple, kiwi, orange, pomegranate, mint leaves, tortilla sheet, oil"
202,pista chocolate & mandarin,Dessert,veg,"Pistachios, milk, sugar, broken rice, green cardamom, white chocolate, milk, egg yolks, whipped cream, vanilla pod, mandarin, sugar, water"
203,banana and chia tea cake,Dessert,veg,"Banana, Castor Sugar, Flour, Oil, Milk, Eggs, Baking Soda, Flax Seeds, Almond Flakes, Chia Seeds"
204,chocolate and almond rum ball ,Dessert,veg,"Chocolate sponge eggless, dark chocolate, single cream, almonds, castor sugar, instant coffee powder, dark rum"
205,lemon sushi cake,Dessert,veg,"Vanilla pre mix, gel, oil, water, egg yolks, lemon juice, sugar, butter, white chocolate, cooking cream, milk"
206,chocolate doughnut,Dessert,veg,"Sugar, egg yolks, egg, butter, yeast, milk"
207,spiced almond banana jaggery cake,Dessert,veg,"Butter, cinnamon molasses powder, nutmeg (powdered), almonds, sugar, eggs, orange peel, banana, flour, baking soda, baking powder, salt, buttermilk, powdered cinnamon"
208,fennel scented sweet banana fritters,Dessert,veg,"Wheat flour, banana, jaggery, milk or water, ghee or oil"
209,camel milk cake tart,Dessert,veg,"Camel milk, sugar, vinegar, butter, brown sugar, maida, eggs"
210,quinoa coconut crumble custard,Dessert,veg,"Knoia (cooked), oats, cinnamon powder, salt, brown sugar or jaggery, nuts, coconut nuts, eggs, kinoia, coconut milk, maple syrup, vanilla extract, cinnamon powder, salt, honey"
211,lamb barley pot,Healthy Food,non-veg,"pot barley, onions, worcestershire sauce, chilli flakes, mustard seeds, thick mutton chunks, thick neck of lamb chops, water or stock (to cover), salt, black pepper (freshly ground)"
212,al hachi chicken,Indian,non-veg,"shallow fried chicken, bottle gourd (boiled and sun dried), onion, garlic, whole spices:, green cardamom, black cardamom, cinnamon sticks, turmeric, deggi mirch, fennel seeds powder, dry ginger powder, coriander powder, salt, mustard oil, desi ghee"
213,berry parfait hazelnut white chocolate sable,Dessert,veg,"for berry parfait:, egg yolk, caster sugar, berry puree, cream cheese, double cream, for hazelnut streusel:, ground hazelnut, flour, caster sugar, butter, for hazelnut white chocolate pressed sable:, hazelnut streusel, cocoa butter, puffed rice, clarified butter, melted white chocolate, for flexy berry:, raspberry puree, sugar, liquid glucose, pectin"
214,badam papite ke kebab with pineapple salsa,Indian,non-veg,"Raw papaya, raw potato, almonds, salt, asafoetida, turmeric, celery, coriander, ginger, green chillies, gram flour, green coriander, oil, pineapple, onion, green chillies, green coriander, lemon juice, salt, pepper"
215,mixed vegetable soup,Healthy Food,veg,"Mix vegetable (tomatoes, carrots, peas and French beans), salt, cumin powder, oil, curry leaves"
''',
'''
216,duo of chocolate and strawberry,Dessert,veg,"dark chocolate, white chocolate, strawberries"
217,mustard-parmesan whole roasted cauliflower,Healthy Food,veg,"cauliflowers, garlic, halved, olive oil , dijon mustard , kosher salt , freshly ground black pepper , fresh parsley leaves, parmesan , lemon wedges"
218,hassel back sweet potatoes,Healthy Food,veg,"sweet potatoes, butter, brown sugar, pure vanilla extract, ground cinnamon, himalayan pink salt / rock salt"
219,mother christmas cake,Dessert,veg,"tart apples (2 large), sugar, apple juice, eggs, vegetable oil, vanilla extracts, all-purpose flour, apple pie spice (cinnamon), salt, pecans, candied red cherries (halved), candied green cherried (halved), candied pineapple (diced), cashews (optional)"
220,matcha tea macarons,Dessert,veg,"egg whites, breakfast sugar, icing sugar, almond powder, matcha powder, heavy cream, white chocolate"
221,"amaranthus granola with lemon yogurt, berries and marigold",Healthy Food,veg,"popped amaranthus (cholai), oats, almonds, cinnamon powder, sunflower seeds, sesame seeds, honey, brown sugar, salt, olive oil, lemon rind, plain yogurt (whipped with lemon rind), blueberries"
222,chocolate fudge cookies,Dessert,veg,"dark chocolate coverture, butter, sugar, eggs, flour, baking powder, salt, cocoa powder, vanilla essence"
223,veg summer rolls,Thai,veg,"rice paper sheets, iceberg lettuce, carrot, bean sprouts, cucumber, tofu, basil, mint leaves, coriander, rice noodles (soaked in warm water for 20-25 minutes), peanuts, hoisin sauce, peanuts, garlic, oil, red chillies, water"
224,eggless vanilla cake,Dessert,veg,"maida, baking powder, castor sugar, butter, milk, vanilla essence, vinegar"
225,sweet potato pie,Dessert,veg,"yams (red skinned), condensed milk, sugar, egg , cinnamon , marshmallows ,"
226,wok tossed asparagus in mild garlic sauce,Healthy Food,veg,"asparagus, 1 fried onion (medium), 1/2 tsp breakfast sugar, 10 ml potato starch, 20 ml stock vegetarian, 20 gm porcini, salt to taste, 50 ml oil"
227,cinnamon oatmeal pancakes,Healthy Food,veg,"rolled oats, buttermilk (divided), whole wheat flour or oat flour, baking powder, baking soda, cinnamon, salt, eggs, canola oil , honey or maple syrup,"
228,chocolate chip cheesecake,Dessert,veg,"butter biscuits (broken into pieces), butter (softened), cream cheese (softened), sugar, egg, rose essence or vanilla essence, chocolate chips"
229,chocolate lava cake,Dessert,veg,"dark chocolate, butter, icing sugar, egg yolks + whole eggs, flour"
230,eggless coffee cupcakes,Dessert,veg,"maida/ flour, baking powder, sugar, cocoa powder, vanilla essence, butter (softened, salted. in case you are using unsalted butter, add 1/4 tsp salt), milk (to make the batter smooth. adjust the milk quantity according to your batter's smoothness), coffee powder + 1 tsp water, to make a paste (you can increase or decrease according to your coffee tolerance)"
231,chicken in white wine,Italian,non-veg,"black pepper, plain flour, olive or sunflower oil, rashers lean bacon, onions or shallots (cut in half), mushrooms, butter, boneless and skinless chicken breasts (chopped into 3cm pieces), dry white wine, chicken or vegetable stock, garlic cloves, bay leaves, fresh thyme sprigs (washed or 1/2 tsp dried thyme)"
''',
'''
232,apple and walnut cake,Dessert,veg,"Apple, Eggs, Walnuts, Sugar, Walnuts, Oil, Flour, Baking Powder, Cinnamon Powder"
233,gluten free almond cake,Healthy Food,veg,"Almond Powder, Egg, Honey, Baking Soda, Vanilla Essence, Salt, Honey, Almond"
234,cinnamon star cookies,Dessert,veg,"Butter, Castor Sugar, Christmas Mix Spicy, Cinnamon Powder, Honey, Glucose, Cream, Poultry Flour, Baking Soda, Bread Flour"
235,whole wheat cake,Healthy Food,veg,"Oven temperature, wheat flour, jaggery sugar, baking powder, oil, eggs, water, almond essence, walnuts"
236,plum cake,Dessert,veg,"oven temp: 150 c-300 f, butter, sugar, eggs, almonds, vanilla essence, mixed fruits (sultanas, raisins, candied peels and cherries), refined flour,"
237,double chocolate easter cookies,Dessert,veg,"Butter, Brown Sugar, Castor Sugar, Vanilla Essence, Dark Chocolate, Refined Flour, Cocoa Powder, Baking Soda, Salt, Milk, Cadbury Gems"
238,holi special malai kofta,Indian,veg,"potatoes, paneer (cottage cheese), maida, coriander leaves (chopped), onion, ginger-garlic paste, tomatoes, malai or cream, raisins and cashew nuts, cashew nuts paste, haldi, red chilli powder, kitchen king masala, kasuri methi (dry fenugreek), salt, sugar"
239,homemade gulab jamun,Dessert,veg,"sugar, water, milk, cardamom seeds, saffron, cardamom powder, khoya, baking soda, maida, milk"
240,lamb rogan josh,French,non-veg,"lamb chops or stewing lamb, vegetable oil, cassia bark or cinnamon stick, bay leaves, green cardamoms, onions, garlic cloves, butter, turmeric, chilli powder, ground cumin, ground coriander, tomato puree, salt, garam masala, lemon juice"
241,fish curry,Thai,non-veg,"fresh sole fish, black pepper powder, lemon (juiced), onion, coriander seeds, black pepper, raw rice, garlic cloves, coconut, coriander leaves, ginger (large), cinnamon powder, clove powder, ground nut oil, tamarind paste, cooking oil, salt,"
242,rice kheer,Indian,veg,"milk, rice (washed), sugar, raisins, green cardamoms, almonds (shredded)"
243,assorted rice kheer sushi,Japanese,veg,"basmati rice, milk, sugar, pistachio, almonds, green cardamoms(powdered), saffron, rose water, rose petals (dried), dark chocolate"
244,jalebi with fennel yogurt pudding,Dessert,veg,"all purpose flour, yogurt, oil, sugar, water, saffron, green cardamom, yogurt (strained), milk (warm), sugar, nutmeg, cardamom powder"
245,broccoli souffle,Italian,veg,"broccoli, butter, extra virgin olive oil, all-purpose flour, low fat milk, salt, black pepper, cheddar cheese, eggs (separated), egg whites, cream of tarter"
246,christmas dry fruit cake,Dessert,veg,"butter (at room temperature), dark brown sugar, eggs, flour, salt, all spice powder, cinnamon, nutmeg, currants; golden raisins; dark raisins (each), soft dried figs, dates (pitted), prunes (stoned dried), apricots (dried), almonds (chopped), brandy, instant espresso (mixed with 1 tbsp water)"
247,microwave chicken steak,Healthy Food,non-veg,"chicken breasts (boneless), eggs (slightly whisked), ginger paste, garlic paste, onions, coriander leaves, green chillies, black pepper powder, flour, vinegar, salt, oil"
248,cheese and ham roll,Snack,veg,"hung curd, butter, cream, ground pimento, lemon juice, vodka, salt and pepper, asparagus spears(cooked), ham, pineapple slices"
249,vegetable manchurian,Chinese,veg,"mixed vegetables - chopped fine or grated, eggs (slightly beaten), refined flour, garlic paste, ginger paste, water, oil , garlic , onions , capsicum, cornflour (blended with water), vinegar, salt, soya sauce, tomato puree, celery, ajinomoto (optional), water"
250,jerk chicken,Indian,non-veg,"chicken legs, lime (halved), jerk seasoning powder (bottled), jerk seasoning paste (bottled), olive oil"
251,lemon poppy seed cake ,Dessert,veg,"Flour, Baking Powder, Salt, Castor Sugar, Baking Soda, Eggs, Butter, Vanilla Essence, Lemon Juice, Poppy, Lemon Peel, Lemon Syrup, Wiped Cream, Fresh Berry"
252,steam bunny chicken bao ,Japanese,non-veg,"Buns, Flour, Dry Yeast, Sugar, Salt, Hot Water, Chicken Mince, Eggs, Soy Sauce, Sugar, Sesame Oil, Worcestershire Sauce, Chives, Aromat Powder"
253,double chocolate easter cookies ,Dessert,veg,"Butter, Brown Sugar, Castor Sugar, Vanilla Essence, Dark Chocolate, Refined Flour, Cocoa Powder, Baking Soda, Salt, Milk, Cadbury Gems"
254,orange quinoa sevaiyan,Healthy Food,veg,"sevaiyan, quinoa, orange juice , dried figs, sugar, almond milk, desi ghee, jaggery, walnuts, melon seeds, peanuts"
255,spicy creamy kadai chicken,Indian,non-veg,"chicken, ginger-garlic paste, pepper powder, lime juice, oil, salt, tomatoes, green chillies, ginger-garlic paste, chilli powder, black cardamoms, cloves, water, onion, ginger, green chillies, chilli powder, turmeric powder, garam masala, kasturi methi, cream"
256,apple kheer,Dessert,veg,"apples, basmati rice, nuscovado sugar (you can also use normal sugar), cashew nuts and almonds, cassia bark or cinnamon stick, red grapes"
257,ragi oats ladoo (laddu),Dessert,veg,"ragi flour, oats flour, dates (ripe), milk, honey, ghee, green cardamom powder, white sesame seeds, coconut powder, cashew nuts"
258,lamb korma,Indian,non-veg,"onions, almond paste, ghee, cinnamon sticks, green cardamom, cloves, mace, bay leaves, garlic paste, ginger paste, lamb, salt, rose water (infused with 4-5 strands of saffron), yellow chilli powder, yogurt, yellow chilli powder, black pepper powder, coriander seed powder, cumin powder, red chilli powder, turmeric powder, clove powder, green cardamom powder, rose petal powder, nutmeg powder, black cardamom powder, fennel powder, cinnamon powder, mace powder, onions, cream/malai"
259,ragi coconut ladoo (laddu),Dessert,veg,"finger millet flour (ragi), jaggery, peanuts, coconut, salt"
''',
'''
260,quick chicken curry,Indian,non-veg,"Chicken, onion paste, tomato, garlic paste, ginger paste, coriander powder, cumin powder, turmeric powder, red chilli powder, garam masala powder, oil, salt, green coriander"
261,chicken shaami kebab,Indian,non-veg,"Chana Dal, Chicken Thai, Salt, Whole Red Chillies, Cumin, Whole Coriander, Cloves, Pepper Whole, Cinnamon Stick, Celery, Eggs, Green Coriander, Mint, Green Chillies, Ginger, Garlic Buds, Oil"
262,chicken masala,Indian,non-veg,"Chicken, ginger, garlic, onion, tomato, garam masala, bay leaves, salt, turmeric, coriander powder, red chilli powder, oil, green coriander, cream"
263,holi special bhang pakode,Indian,veg,"besan, potato, fresh bhang leaves, spinach, bhang seed powder, ajwain, fresh green chilly , salt, tamarind paste, red chilly powder, mustard seeds, whole red chilli, soda"
264,kuttu atta pizza,Italian,veg,"kuttu atta, salt, sugar, yeast, mozzarella cheese fresh, tomato, basil, cottage cheese, green chillies, olive oil, salt, black pepper (crushed), oregano"
265,arbi kofta with mint yogurt dip,Snack,veg,"arbi/colocasia roots, water chestnut flour (kuttu ka aata), green chili, ginger, carom seeds, rock salt, oil, mint, curd, cucumber, pomegranate"
266,puffed rice squares,Snack,veg,"puffed rice, nuts, honey, jaggery, butter, kewda to flavor, cardamom powder"
267,red velvet banana pudding,Dessert,veg,"one can of sweetened condensed milk, ice cold water, instant vanilla pudding mix, cream cheese (softened and cut into 8 pieces), heavy cream, one 9 x 13 inch layer of red velvet cakcake, ripe bananas, mini chocolate chips, sugar, cocoa, cake flour, baking soda, salt, butter (room temp cut into 1 inch pieces), eggs, milk, sour cream, cider vinegar, vanilla extract, red food coloring, all-purpose flour, milk, unsalted butter (room temperature), sugar, vanilla extract"
268,baked wild berry cheesecake,Dessert,veg,"butter, digestive biscuits, berries, cream cheese, castor sugar, vanilla extract, egg (lightly beaten), icing sugar"
269,spiced orange valencia cake,Dessert,veg,"egg whites, egg white powder, sugar, almond powder, hazelnut powder, sugar, hazelnut (toasted)"
270,jalapeno cheese fingers,Mexican,veg,"yellow cornmeal, sugar, baking soda, salt, buttermilk (well-shaken), egg, cheddar (extra sharp), scallion (white and pale green parts only), pickled jalapenos (drained), unsalted butter,"
271,californian breakfast benedict,Snack,veg,"brioche loaf, avocado paste, eggs, tomato, spinach, nutmeg powder, phyllo pastry sheet, assorted seasonal fruits, hollandaise sauce"
272,chocolate marquise,Dessert,veg,"dark chocolate (melted), castor sugar, egg yolk, egg, cocoa powder, coffee, cream, berries, dark chocolate, fresh cream"
273,corn & jalapeno poppers,Mexican,veg,"fresh corn kernels, corn flour, whole egg, cheddar cheese, jalapeno poppers, smoked paprika, coriander (toasted & ground), green onions, fresh cilantro, lemon (zest and juice), cooking oil"
274,banana phirni tartlets with fresh strawberries,Snack,veg,"basmati rice (soaked in water), milk, cardamom powder, milk, saffron, sugar, banana, fresh strawberries, plain flour, butter (chilled), castor sugar, egg yolk, chilled water"
275,mexican pizza,Mexican,veg,"Dough tortia, refried beans, bell paper, spring onion, lettuce, mozzarella cheese, orange cheddar cheese, chitpole dressing, for pico de chelo, tomato, onion, lemon juice, salt, green chilli, coriander, black beans (boiled ), Tomato, onion, vine paper, vegetable oil"
276,apple and pear cake,Healthy Food,veg,"Core, Chopped and Sliced ??Apple, Core, Chopped and Sliced ??Pears, Castor Sugar, Vanilla Essence, Sunflower Oil, Eggs, Flour, Milk, Baking Powder, Milk, Cinnamon Stick, Egg yolks, Castor Sugar"
277,microwave chocolate cake,Dessert,veg,"Flour, castor or powdered sugar, oil, butter or margarine, cocoa powder, water, vanilla essence, baking soda, baking powder, salt, egg"
278,white chocolate and lemon pastry,Dessert,veg,"White chocolate, fresh cream, VIP cream, vanilla bean, vanilla extract, cream cheese, gelatin, lemon, egg yolks, butter, castor sugar"
279,mixed beans salad,Healthy Food,veg,"mixed boiled beans (choose from rajma, chawli, chick peas, hara chana), spring onions, tomatoes (diced), oil, lemon juice, basil, garlic, salt and pepper, for garnish:, coriander"
280,baked raw banana samosa,Snack,veg,"onion, ginger, curry powder, fresh coriander, green chilli, raw banana paste, refined oil, mustard seeds, phyllo sheets, salt"
281,coconut mango oatmeal with cinnamon hint,Healthy Food,veg,"coconut (tender), coconut milk, oats, ripe mango (diced), castor sugar, dry fruits, honey, cardamom powder"
282,fruit cube salad,Healthy Food,veg,"watermelon, cantaloupe, kiwifruiit, pineapple, marshmallow, mint leaf (crushed nuts, sesame seeds or cinnamon)"
283,veg hakka noodles,Chinese,veg,"noodles, salt, oil, garlic paste, ginger paste, beans, cabbage, carrot, spring onion, capsicum, soy sauce, green chilli sauce, tomato sauce"
284,strawberry quinoa pancakes,Healthy Food,veg,"quinoa, milk, olive oil, egg (slightly beaten), baking powder, orange essence, castor sugar, maple syrup, strawberries (to garnish)"
285,spinach & banana pancakes,Healthy Food,veg,"Rolled Oats, Milk, Spinach, Banana, Egg, Cinnamon Powder, Vanilla Extract, Baking Powder"
286,french onion grilled cheese,French,veg,"Brown slice bread, onion, oil, emmental cheese"
287,pasta in cheese sauce,Italian,veg,"Milk, Flour, Butter, Pepper Powder, Nutmeg, Cheese, Pasta (of your choice)"
288,deviled scotch egg,French,non-veg,"Lamb Keema, Rosemary, Thyme, Eggs (hard boiled peel), Flour, Eggs (Lightly Whipped), Panco, Peanut Oil, Salt, Pepper, Mayonnaise, Apple Cedar Vinegar, English Mustard, Salt, Pepper, Paprika and Olive Powder"
289,amritsari fish,Indian,non-veg,"fish with curry, ginger and garlic"
290,butter chicken,Indian,non-veg,mughalai delecacy
291,chicken razala,Indian,non-veg,chicken cooked in a rich gravy with mint
292,chicken tikka,Indian,non-veg, served on a skewer
293,chicken tikka masala,Indian,non-veg,chicken roasted in a yogurt tomato sauce. creamy texture.
294,mushroom matar,Indian,veg,mushroom and peas in a masala/chili sauce
295,tandoori chicken,Indian,non-veg,as a dish originated in the punjab before the independence of india and pakistan.
296,tandoori fish tikka,Indian,non-veg,chickenn lime and ginger and cooked over an open fire.
297,chettinadu chicken,Indian,non-veg,chicken and spices
298,chicken 65,Chinese,non-veg,"ed chicken preparation. chicken, onion, ginger"
299,kolim / jawla,Indian,veg,dried fish named kolim or jawla found in coastal maharashtra with onion and spices. usually eaten with bhakri or chapati
''',
'''
300,black rice,Healthy Food,veg,variety of rice
301,brown rice,Healthy Food,veg,variety of rice.
302,koldil chicken,Chinese,non-veg,made with banana flower; an assamese specialty
303,red rice,Healthy Food,veg,variety of rice.
304,rice,Indian,veg,boiled rice
305,sunga pork,Japanese,veg,curry
306,banana chips,Snack,veg,"dried slices of bananas (fruits of herbaceous plants of the genus musa of the soft, sweet ""dessert banana"" variety), they can be covered with sugar or honey and have a sweet taste, or they can be fried in oil and spices and have a salty and/or spicy taste.[2]"
307,bhurji- egg,Indian,non-veg,"made using indian spices, onion, tomatoes, green chilli, and had with bread, or parathas."
308,flattened rice / poha,Indian,veg,"dehusked rice which is flattened into flat light dry flakes, these flakes of rice swell when added to liquid, whether hot or cold, as they absorb water, milk, or any other liquids. the thicknesses of these flakes vary between almost translucently thin (the more expensive varieties) to nearly four times thicker than a normal rice grain."
309,puffed rice,Snack,veg,"grain made from rice; usually made by heating rice kernels under high pressure in the presence of steam, though the method of manufacture varies widely. pori (puffed rice) has been mentioned in various tamil literatures as an offering to hindu deities. offerings of pori and jaggery made to vinayagar (lord ganesh) are mentioned in the tiruppugazh, a 15th-century anthology of tamil religious songs, written by tamil poet arunagirinathar. pori is offered to hindu gods and goddesses in all poojas in the south indian states of kerala and tamil nadu."
310,Miso-Butter Roast Chicken With Acorn Squash Panzanella,Japanese,non-veg,"chicken, acorn squash,sage, rosemary, butter"
311,Honeydew Salad with Ginger Dressing and Peanuts,Healthy Food,veg,"peeled ginger, lightbrown sugar,chilli, honeydew melon,cucumber, avacado"
312,Kimchi and Miso Noodle Soup,Korean,veg,"scallions, cloves of garlic,cabbage kimchi, tofu "
313,Spicy Korean Steak,Korean,non-veg," boneless steak, olive oil, black pepper, oyster sauce,  ginger, chilli flakes, cooking wine, kimchi,cilantro"
314,French Spiced Bread,French,veg,"all purpose flour, butter, dried appricots, honey, milk dried plumps, sugar,salt"
315,Quinoa Bowl and Berries,Healthy Food,veg,"quinoa, black berries,strawberries, blueberries,,chia seeds, almonds"
316,Shawarma-Spiced Braised Leg of Lamb,Indian,non-veg,"cumin seed, garlic, chilli powder, lamb leg, corriender, onion, turmeric powder, lemon, tomato"
317,Roast Pork Tenderloin with Carrot Romesco, Korean,non-veg,"carrots, Olive Oil, Salt ,  pork tenderloin, Garlic, red pepper flake, red wine vineger, "
318,"Ricotta Gnocchi with Asparagus, Peas, and Morels",Italian,veg," ricotta,Asparagus,  morel mushrooms, Olive Oil,  Parmesan, fresh peas, butter, black pepper,  shallot, "
319,Crispy Pakora,Indian,veg,"Cabbage, carrot, onion, gram flour"
320,Lamb Tikka,Indian,non-veg,"Boneless Lamb, Turmeric powder, corriender powder, cumin powder, yogurt, garlic, giner"
321,Grilled Sweet Prawn,Chinese,non-veg,"Prawn, teriyaki sauce, salmon, avacado, cucumber"
322,Pho Tai rare beef,Vietnames,non-veg,"Bean Sprouts, lemon, Thai basils, Rice noodles, beef"
323,Summer Rolls,Vietnames,non-veg,"Mint, Lettuce, Noodles, Prawn, Rice Paper,Peanut Sauce"
324,Spice Chicken Baugette,Vietnames,non-veg,"Spice Chicken, cucumber, coriander, pickled carrort, mayo"
325,Bean Curd Rolls,Vietnames,veg,"bean curd,mix herbs, lettuce, cucuber, rice paper"
326,Pho Chay Soup,Vietnames,veg,"Rice noodle,vegatable soup, bean curd, mushroom"
327,Pho Ga Chicken,Vietnames,non-veg,"Rice noodle, chicken, lemon, bean sprouts, Thai basils, chicken"
328,Chicken Sweet Corn Soup,Chinese,non-veg,"Chicken,Chicken brouth, Sweet corn, garlic, ginger"
329,Thai Spareribs,Thai,non-veg," lemongrass, ginger, meaty sparerib, Sesame-Cilantro Rice,peanut sauce,sesame oil,garlic, soy sauce "
330,Frenched Green Beans,French,veg," green beans, Olive Oil, black paper, vineger,"
331,Lemony Crab Salad with Baby Greens,Healthy Food,non-veg,"Lemon juice, olive oil, crab, lecttus, paper,salt, vineger"
332,Mushroom Manchruian,Indian,veg,"Mushroom, Panner, Soy sauce, ketchup, Viniger,onion, corriender, Indian Spices"
333,Biryani,Indian,non-veg,"Chicken, Rice, Cinamon, Clove, ginger, garlic, yougurt, turmeric powder, cumin powder, corriender powder"
334,Tandoori Chicken,Indian,non-veg,"Cicken, yougurt, tandori spices, ginger, coriander, turmeric, lime"
335,Shrimp Olivier,French,non-veg,"Shrimp, egg, Potatoes, carrot, onion, pasley, mayo"
336,Potato Casserole,Italian,veg,"potatoes, butter, salt, pepper"
337,Thyme-Roasted Sweet Potatoes,Healthy Food,veg,"sweet potatoes, thyme leaves, olive oil, red papper flakes,"
338,Noodle Curry,Vietnames,non-veg,"Vegetable stock curry, coconut, lime leaves, raddish, carrot"
339,Grill Lemon grass Pork baguette,Vietnames,non-veg,"Lemon grass, pork, coriender,cucumber, pickeled carrot, chilli"
340,Sukuti Chatpate,Nepalese,non-veg,"crunchy noodles, onion, cucumber,tomatoes, lemon juice, puffed rice, dried meat"
341,Cheese Naan,Indian,veg,"Aall purpose flour, yougurt, cheese"
342,Mushroom Rice,Nepalese,veg,"Mushroom, Rice, Cumin Seeds"
343,Bringle Alo,Nepalese,veg,"aubergine,potato, garlic, ginger, cumin seeds, spices"
344,Mutar Paneer,Indian,veg,"Green pea, cottage cheese, garlic, indian spices"
345,Cucumber and Radish Salad,Healthy Food,veg,"cucumber,raddish,vinegar, coriander,olive, salt papper"
346,Channa Masala,Indian,veg,"chickpeas, turmeric powder, onion, ginger, garlic, curry powder"
347,Saag Alo ,Nepalese,veg,"Spinach, onion, potato, cumin seed, turmeric powder, nepali spices"
348,Alo Tama Bodi,Nepalese,veg,"bamboo shoot, black eye bean, potato"
349,Tarka Daal,Nepalese,veg,"yello lentils,garlic, cumin seed, butter"
''',
'''
350,Jeera Alu,Nepalese,veg,"boiled potatoes, cumin seeds, lemon juice"
351,Nepali Chicken Curry,Nepalese,non-veg,"boneless chicken, onion, tomato, coriender powder,cumin powder,butter,turmeric, chilli powder, garlic,ginger"
352,Lamb Shashlik,Indian,non-veg,"minced lamb marinated with indian spices, garlic, ginger, coriander, yogurt, turmeric, cloves"
353,Hyakula,Nepalese,non-veg,"lamb ribs, cumin powder,turmeric powder,nepali spices, mustard oil "
354,Alo Achar,Nepalese,veg,"boiled potatoes, peas, cucumber, mustard oil, turmeric powder, cumin powder, carrot, salt"
355,Chicken Momo,Nepalese,non-veg,"minced chicken meat, coriender, cumin powder,garlic,ginger,onion,flour wrapping"
356,Black-Bean Burgers,Chinese,veg,"cumin, black bean, cilantro, lettuce,sour cream, oregano, buns"
357,Parmesan Toasts,Italian,veg,"Bread, garlic, olive oil, Parmesan cheese, salt"
358,Rice with Soy-Glazed Bonito Flakes and Sesame Seeds,Japanese,non-veg,"sake, sesame seeds, soy sauce, rice, japanese sauces"
359,Shirazi Salad,Healthy Food,veg,"Spring onion, cheese, lemon juice, cucumber, onion, carrot, parsley, cilantro"
360,Sesame Noodles with Chili Oil and Scallions,Chinese,veg,"Noodles, Salt,garlic,chilli oil, sesame oil, chilli flakes, scallions, sichuan pepper, vinegar, soy sauce"
361,Thai Green Curry ,Thai,veg,"cumin seeds, coriander seeds, chillies, garlic, ginger onion, thai sauces,lemon grass, penut "
362,Ground Pork Menudo,Spanish,non-veg,"onion, garlic, olive oil, minced pork, fish sauce,  green peas, black peper"
363,Bao Bun ,Chinese,non-veg,"sesame seed, all purpose flour, spring onion, teriyaki sauce"
364,Garlic Naan,Indian,veg,"garlic, all purpose flour, yougurt, cumin seed"
365,Egg Curry with Tomatoes and Cilantro,Indian,non-veg,"boiled egg, cilantro, garlic,cucumber,tumeric powder,tomatoes,"
366,Kimchi Bokumbab,Korean,non-veg,"Cabbage Kimchi, Stir fried eggs, rice, seaweed, sesame seeds, spring onion"
367,Korean fried Chicken,Korean,non-veg," korean sauce, boneless chicken,sesame seeds"
368,Prawn kastu Curry,Japanese,non-veg,"prawn, rice, japanes curry sauce, bread crumbs, rice"
369,Beef Bibimbab,Korean,non-veg,"Beef,Cucumber,carrot, mushrooms,Spinich,Rice, Gochujang, Soy sauce"
370,Sweet and Sour Chicken Fried Rice,Chinese,non-veg," Rice, carrot, peas, chicken, soy sauce, sugar, garlic, capcicum"
371,Sea Food Soup,Chinese,non-veg,"Prawn,Squid, fish ball, fish cake, mussels, crab sticks"
372,Pad Thai,Thai,non-veg,"noodles, vegetable oil, garlic, eggs, lime juice , brown sugar, fish sauce, ginger,red pepper flakes, onion, cilantro, penuts"
373,Spicy Kimchi Tofu Stew,Korean,veg,"tofu, kimchi, gochujang,black pepper,  sesame seeds, soy sauce, scallions"
374,Slow-Roasted Pork ,Korean,non-veg,"fresh sage,garlic cloves, bone-in pork shoulder,ground pepper,Dijon mustard"
375,Pico de Gallo Verde,Mexican,veg,"avacado, tomato, cucumber,celery, garlic, mint, lemon juice, chillies, onion, cilantro"
376,Pineapple-Coconut Rice,Thai,veg,"brown rice, coconut milk, onion, carrot, cashew, pineapple, vegetable oil, ginger, curry powder"
377,Lamb and Green Squash Dumplings,Chinese,non-veg,"Squash, zucchini, scallions, soya sauce, ginger, cooking wine, vineger, all purpose flour, sichuan peppercorns,ground lamb,"
378,Crispy Tofu Balls,Japanese,veg," tofu, scallions, mushrooms,Spicy aioli,corn, white pepper, vegetable oil"
379,Grilled Chicken with Almond and Garlic Sauce,Healthy Food,non-veg,"lemon juice, olive oil, mushrooms lemon zest, chicken breast, roasted almonds, garlic"
''',

'''
380,Parmesan Cauliflower and Parsley Salad,Italian,veg,",olives, parmesan cheese, pasley,pepper,oil"
381,Vietnamese Chicken Salad,Vietnames,non-veg,"roasted peanuts,basil leaves, mint leaves, chicken, cucumber,carrot"
382,Eggplant and Beef Stir-Fry,Thai,non-veg,"soya sauce,mint,thai chillies,vermicelli noodles,beef, asaian eggplat"
383,Stir-Fried Lettuces With Crispy Shallots,Chinese,non-veg,"sliced shallots,pepper,salt,garlic, ginger, lettuce,brown rice"
384,Chicken and Dumplings,Chinese,non-veg,"purpose flour,egg,nutmeg, chicken broth, carrot,salt,chives, pepper, chicken thighs"
385,Asian Salmon Bowl with Lime Drizzle,Thai,non-veg," jasmine rice, garlic, butter, soy sauce, salmon fillet,spinach,black sesame seeds"
386,Pasta with Garlic-Scape Pesto,Italian,veg,"pistachios, Parmigiano-Reggiano cheese,salt and black pepper, spaghetti,olive oil"
387,Pico de Gallo,Mexican,veg,"onion,tomatoes, oil,  cilantro, jalapeao"
388,Basmati Rice with Summer Vegetable Salad,Indian,veg,"basmati rice,shallot,radishes,greens, sprouts, tomatoes, peas, summer squash,carrot, oil,salt"
389,Fresh Corn Tortillas,Mexican,veg,"corn tortilla mix,corn,salt"
390,Quinoa Tabbouleh,Healthy Food,veg," quinoa, olive oil, tomato,  cucumber, parsley, mint, scallions, thinly sliced"
391,Grilled Clams With Herb Butter,French,non-veg," parsley, pepper, salt, scallion, lemon juice, littleneck clams"
392,Rajas Poblanas,Mexican,veg,"poblano pepper, cream, salt, cream cheese"
393,Braised Beef Short Ribs,Korean,non-veg,"Beef, Scallion, Raddish, Spanich "
394,Fig and Sesame Tart with Cardamom Orange Cream,Dessert,non-veg," all-purpose flour,sugar,salt,unsalted butter, egg yolk,heavy cream, cinnamon,orange zest, fig,sesame seeds, mild honey"
395,Rouille,French,veg," bread crumbs,cayenne, extra-virgin olive oil,coarse sea salt, garlic"
396,Kimchi Toast,Korean,veg," cream cheese, chopped kimchi, scallions,country-style bread, sesame seeds,  cilantro leaves"
397,"Tacos de Gobernador (Shrimp, Poblano, and Cheese Tacos)",Mexican,non-veg,"poblano chiles, bacon, shrips, red salsa, garlic, corn tortillas, lime juice"
398,Melted Broccoli Pasta With Capers and Anchovies,French,non-veg,"broccoli,Bread Crumbs,  anchovy fillets, garlic cloves,  red pepper flakes, penne pasta, olive oil"
399,Lemon-Ginger Cake with Pistachios,Dessert,non-veg,"egg yolks,lemon juice, unsalted butter, all purpose flour, sugar, ginger, milk"
400,Rosemary Roasted Vegetables,Healthy Food,veg,"kosher salt, rosemary, garlic, potato, olive oil, carrot, walnut, cheese, ground pepper"
''']


prompt_parts = [
  f'''SYSTEM PROMPT:You recommend one Name of food based on user's requirement, users choice and available healthy options chose from one of the healthy options give detailed cooking instruction for selected dish [Include the  food ID from the food selected from the available options OUTPUT SHOULD LOOK LIKE THE ASSISTANT RESPONSE EXAMPLE],
     USER'S REQUIREMENT: above 15000cal ,male,needs more energy, can eat veg and non-veg foods,
     USER'S CHOICE: I want Eba and Egusi soup,
     AVAILABLE HEALTHY OPTIONS:

Food_ID,        Name_of_Food,         C_Type,     Veg_Type,         Description:
{Available_options[6]}
ASSISTANT RESPONSE EXAMPLE: [Food number(FOOD ID), Food (FOOD NAME), Ingredients ...., cooking instructions ...]
'''
]
response = genai.generate_text(prompt=prompt_parts[0],max_output_tokens=2024,temperature=1)
print(response.candidates[0]["output"])


# prompt_check = [
#   f'''SYSTEM PROMPT: you recommend one Name of food based on user's requirement, users choice and available healthy options chose from one of the healthy options instead of explaining what the user wants [Include the  food ID from the food selected from the available options],
#      USER'S REQUIREMENT: Below 15000cal ,male,needs more energy, can eat veg and non-veg foods,
#      USER'S CHOICE: I want Beans and plantain,
#      AVAILABLE HEALTHY OPTIONS:

# Food_ID,        Name_of_Food,         C_Type,     Veg_Type,         Description:
# {Available_options[5]}
# '''
# ]
# prompt_response = genai.generate_text(prompt="prompt_parts[0]",max_output_tokens=2024,temperature=1)
# print(response.candidates[0]["output"])

# print(Available_options[4])