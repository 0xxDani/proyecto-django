from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES=(
    ('RD', 'Ropa Dama'),
    ('ME', 'Maquillaje'),
    ('CD', 'Calzado Dama'),
    ('PD', 'Perfumería Dama'),
    ('AD', 'Accesorios Dama'),
    ('PH', 'Productos para el hogar'),
    ('BS', 'Bolsos'),
    ('ES', 'Electrodomésticos'),
    ('JA', 'Juguetería'),
    ('AE', 'Arte'),
    ('PL', 'Productos de aplicacion corporal'),
    ('NP', 'Novedades y promociones'),
    ('CS', 'Chaquetas'),
    ('CC', 'Calzado para caballero'),
    ('AC', 'Accesorios Caballero'),
)

STATE_CHOICES = (
    ('Amazonas', 'Leticia'),
    ('Antioquia', 'Medellín'),
    ('Arauca', 'Arauca'),
    ('Atlántico', 'Barranquilla'),
    ('Bolívar', 'Cartagena'),
    ('Boyacá', 'Tunja'),
    ('Caldas', 'Manizales'),
    ('Caquetá', 'Florencia'),
    ('Casanare', 'Yopal'),
    ('Cauca', 'Popayán'),
    ('Cesar', 'Valledupar'),
    ('Chocó', 'Quibdó'),
    ('Córdoba', 'Montería'),
    ('Cundinamarca', 'Bogotá, D.C.'),
    ('Guainía', 'Inírida'),
    ('Guaviare', 'San José del Guaviare'),
    ('Huila', 'Neiva'),
    ('La Guajira', 'Riohacha'),
    ('Magdalena', 'Santa Marta'),
    ('Meta', 'Villavicencio'),
    ('Nariño', 'Pasto'),
    ('Norte de Santander', 'Cúcuta'),
    ('Putumayo', 'Mocoa'),
    ('Quindío', 'Armenia'),
    ('Risaralda', 'Pereira'),
    ('San Andrés y Providencia', 'San Andrés'),
    ('Santander', 'Bucaramanga'),
    ('Sucre', 'Sincelejo'),
    ('Tolima', 'Ibagué'),
    ('Valle del Cauca', 'Cali'),
    ('Vaupés', 'Mitú'),
    ('Vichada', 'Puerto Carreño'),
)

COUNTRY_CHOICES = (
    ('Afganistán', 'Afganistán'), ('Albania', 'Albania'), ('Argelia', 'Argelia'), ('Andorra', 'Andorra'), ('Angola', 'Angola'),
    ('Anguila', 'Anguila'), ('Antigua y Barbuda', 'Antigua y Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Aruba', 'Aruba'),
    ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaiyán', 'Azerbaiyán'), ('Bahamas', 'Bahamas'), ('Baréin', 'Baréin'),
    ('Bangladés', 'Bangladés'), ('Barbados', 'Barbados'), ('Bielorrusia', 'Bielorrusia'), ('Bélgica', 'Bélgica'), ('Belice', 'Belice'),
    ('Benín', 'Benín'), ('Bermudas', 'Bermudas'), ('Bután', 'Bután'), ('Bolivia', 'Bolivia'), ('Bosnia y Herzegovina', 'Bosnia y Herzegovina'),
    ('Botsuana', 'Botsuana'), ('Brasil', 'Brasil'), ('Islas Vírgenes Británicas', 'Islas Vírgenes Británicas'), ('Brunéi', 'Brunéi'), ('Bulgaria', 'Bulgaria'),
    ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Camboya', 'Camboya'), ('Camerún', 'Camerún'), ('Canadá', 'Canadá'),
    ('Cabo Verde', 'Cabo Verde'), ('Caribe neerlandés', 'Caribe neerlandés'), ('Islas Caimán', 'Islas Caimán'), ('República Centroafricana', 'República Centroafricana'),
    ('Chad', 'Chad'), ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Comoras', 'Comoras'),
    ('Congo', 'Congo'), ('Islas Cook', 'Islas Cook'), ('Costa Rica', 'Costa Rica'), ('Croacia', 'Croacia'), ('Cuba', 'Cuba'),
    ('Curazao', 'Curazao'), ('Chipre', 'Chipre'), ('Chequia', 'Chequia'), ('República Democrática del Congo', 'República Democrática del Congo'), ('Dinamarca', 'Dinamarca'),
    ('Yibuti', 'Yibuti'), ('Dominica', 'Dominica'), ('República Dominicana', 'República Dominicana'), ('Timor Oriental', 'Timor Oriental'), ('Ecuador', 'Ecuador'), ('Egipto', 'Egipto'),
    ('El Salvador', 'El Salvador'), ('Guinea Ecuatorial', 'Guinea Ecuatorial'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'),
    ('Etiopía', 'Etiopía'), ('Islas Malvinas', 'Islas Malvinas'), ('Islas Feroe', 'Islas Feroe'), ('Fiyi', 'Fiyi'), ('Finlandia', 'Finlandia'),
    ('Francia', 'Francia'), ('Guayana Francesa', 'Guayana Francesa'), ('Polinesia Francesa', 'Polinesia Francesa'), ('Gabón', 'Gabón'), ('Gambia', 'Gambia'),
    ('Georgia', 'Georgia'), ('Alemania', 'Alemania'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Grecia', 'Grecia'),
    ('Groenlandia', 'Groenlandia'), ('Granada', 'Granada'), ('Guadalupe', 'Guadalupe'), ('Guatemala', 'Guatemala'), ('Guernsey', 'Guernsey'),
    ('Guinea', 'Guinea'), ('Guinea-Bisáu', 'Guinea-Bisáu'), ('Guyana', 'Guyana'), ('Haití', 'Haití'), ('Honduras', 'Honduras'), ('Hong Kong', 'Hong Kong'),
    ('Hungría', 'Hungría'), ('Islandia', 'Islandia'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Irán', 'Irán'),
    ('Irak', 'Irak'), ('Irlanda', 'Irlanda'), ('Isla de Man', 'Isla de Man'), ('Israel', 'Israel'), ('Italia', 'Italia'),
    ('Costa de Marfil', 'Costa de Marfil'), ('Jamaica', 'Jamaica'), ('Japón', 'Japón'), ('Jersey', 'Jersey'), ('Jordania', 'Jordania'),
    ('Kazajistán', 'Kazajistán'), ('Kenia', 'Kenia'), ('Kiribati', 'Kiribati'), ('Kuwait', 'Kuwait'), ('Kirguistán', 'Kirguistán'), ('Laos', 'Laos'),
    ('Letonia', 'Letonia'), ('Líbano', 'Líbano'), ('Lesoto', 'Lesoto'), ('Liberia', 'Liberia'), ('Libia', 'Libia'),
    ('Liechtenstein', 'Liechtenstein'), ('Lituania', 'Lituania'), ('Luxemburgo', 'Luxemburgo'), ('Macao', 'Macao'), ('Macedonia del Norte', 'Macedonia del Norte'),
    ('Madagascar', 'Madagascar'), ('Malaui', 'Malaui'), ('Malasia', 'Malasia'), ('Maldivas', 'Maldivas'), ('Malí', 'Malí'),
    ('Malta', 'Malta'), ('Islas Marshall', 'Islas Marshall'), ('Martinica', 'Martinica'), ('Mauritania', 'Mauritania'), ('Mauricio', 'Mauricio'),
    ('Mayotte', 'Mayotte'), ('México', 'México'), ('Micronesia', 'Micronesia'), ('Moldavia', 'Moldavia'), ('Mónaco', 'Mónaco'), ('Mongolia', 'Mongolia'),
    ('Montenegro', 'Montenegro'), ('Montserrat', 'Montserrat'), ('Marruecos', 'Marruecos'), ('Mozambique', 'Mozambique'), ('Myanmar', 'Myanmar'),
    ('Namibia', 'Namibia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'), ('Países Bajos', 'Países Bajos'), ('Nueva Caledonia', 'Nueva Caledonia'),
    ('Nueva Zelanda', 'Nueva Zelanda'), ('Nicaragua', 'Nicaragua'), ('Níger', 'Níger'), ('Nigeria', 'Nigeria'), ('Niue', 'Niue'),
    ('Isla Norfolk', 'Isla Norfolk'), ('Corea del Norte', 'Corea del Norte'), ('Noruega', 'Noruega'), ('Omán', 'Omán'), ('Pakistán', 'Pakistán'), ('Territorios Palestinos', 'Territorios Palestinos'),
    ('Panamá', 'Panamá'), ('Papúa Nueva Guinea', 'Papúa Nueva Guinea'), ('Paraguay', 'Paraguay'), ('Perú', 'Perú'),
    ('Filipinas', 'Filipinas'), ('Islas Pitcairn', 'Islas Pitcairn'), ('Polonia', 'Polonia'), ('Portugal', 'Portugal'), ('Qatar', 'Qatar'), ('Reunión', 'Reunión'), ('Rumanía', 'Rumanía'), ('Rusia', 'Rusia'), ('Ruanda', 'Ruanda'), ('San Bartolomé', 'San Bartolomé'),
    ('Santa Elena, Ascensión y Tristán de Acuña', 'Santa Elena, Ascensión y Tristán de Acuña'), ('San Cristóbal y Nieves', 'San Cristóbal y Nieves'), ('Santa Lucía', 'Santa Lucía'),
    ('San Martín (parte francesa)', 'San Martín (parte francesa)'), ('San Pedro y Miquelón', 'San Pedro y Miquelón'), ('San Vicente y las Granadinas', 'San Vicente y las Granadinas'),
    ('Samoa', 'Samoa'), ('San Marino', 'San Marino'), ('Santo Tomé y Príncipe', 'Santo Tomé y Príncipe'), ('Arabia Saudita', 'Arabia Saudita'), ('Senegal', 'Senegal'),
    ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leona', 'Sierra Leona'), ('Singapur', 'Singapur'),
    ('San Martín (parte neerlandesa)', 'San Martín (parte neerlandesa)'), ('Eslovaquia', 'Eslovaquia'), ('Eslovenia', 'Eslovenia'), ('Islas Salomón', 'Islas Salomón'),
    ('Somalia', 'Somalia'), ('Sudáfrica', 'Sudáfrica'), ('Georgia del Sur e Islas Sandwich del Sur', 'Georgia del Sur e Islas Sandwich del Sur'), ('Corea del Sur', 'Corea del Sur'), ('Sudán del Sur', 'Sudán del Sur'),
    ('España', 'España'), ('Sri Lanka', 'Sri Lanka'), ('Sudán', 'Sudán'), ('Surinam', 'Surinam'),
    ('Svalbard y Jan Mayen', 'Svalbard y Jan Mayen'), ('Suecia', 'Suecia'), ('Suiza', 'Suiza'), ('Siria', 'Siria'),
    ('Taiwán', 'Taiwán'), ('Tayikistán', 'Tayikistán'), ('Tanzania', 'Tanzania'), ('Tailandia', 'Tailandia'), ('Togo', 'Togo'),
    ('Tokelau', 'Tokelau'), ('Tonga', 'Tonga'), ('Trinidad y Tobago', 'Trinidad y Tobago'), ('Túnez', 'Túnez'), ('Turquía', 'Turquía'),
    ('Turkmenistán', 'Turkmenistán'), ('Islas Turcas y Caicos', 'Islas Turcas y Caicos'), ('Tuvalu', 'Tuvalu'), ('Uganda', 'Uganda'),
    ('Ucrania', 'Ucrania'), ('Emiratos Árabes Unidos', 'Emiratos Árabes Unidos'), ('Reino Unido', 'Reino Unido'), ('Estados Unidos', 'Estados Unidos'),
    ('Islas Ultramarinas Menores de Estados Unidos', 'Islas Ultramarinas Menores de Estados Unidos'), ('Uruguay', 'Uruguay'), ('Uzbekistán', 'Uzbekistán'), ('Vanuatu', 'Vanuatu'), ('Ciudad del Vaticano', 'Ciudad del Vaticano'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Wallis y Futuna', 'Wallis y Futuna'),
    ('Sáhara Occidental', 'Sáhara Occidental'), ('Yemen', 'Yemen'), ('Zambia', 'Zambia'), ('Zimbabue', 'Zimbabue'),
)

STATUS_CHOICES = (
    ('Aceptado','Aceptado'),
    ('Empacado','Empacado'),
    ('En camino','En camino'),
    ('Entregado','Entregado'),
    ('Cancelado','Cancelado'),
    ('Pendiente','Pendiente'),
)

class Product(models.Model):
    titulo_producto = models.CharField(max_length=100)
    precio_venta = models.FloatField()
    precio_con_descuento = models.FloatField()
    descripcion = models.TextField()
    referencia = models.TextField(default='')
    pais_origen = models.CharField(choices=COUNTRY_CHOICES, max_length=60)
    categoria = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    imagen_producto = models.ImageField(upload_to='product')

    class Meta:
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.titulo_producto

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField(default=0)
    departamento = models.CharField(max_length=200)
    identificacion = models.IntegerField()
    ciudad = models.CharField(choices=STATE_CHOICES, max_length=100)

    class Meta:
        verbose_name_plural = "Administradores"

    def __str__(self):
        return self.nombre

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name_plural = "Carrito de compras"

    @property
    def total_cost(self):
        return self.cantidad * self.product.precio_con_descuento

class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id = models.CharField(max_length=100,blank=True,null=True)
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Pagos"

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_orden = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default='Pendiente')
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default="")

    class Meta:
        verbose_name_plural = "Pedidos Realizados"
    @property
    def total_cost(self):
        return self.cantidad * self.product.precio_con_descuento

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Lista de seguimiento"

class ContactMessage(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    indicativo = models.CharField(max_length=5)
    identificacion = models.CharField(max_length=20)
    tipo_caso = models.CharField(max_length=20)
    asunto = models.CharField(max_length=200)
    numero_factura = models.CharField(max_length=50)
    descripcion = models.TextField()

    class Meta:
        verbose_name_plural = "Mensajes de contacto"

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

