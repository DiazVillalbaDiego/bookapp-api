from app.models import Book


def _cover(seed: str) -> str:
    # Imagen de prueba estable (misma imagen para el mismo seed)
    return f"https://picsum.photos/seed/{seed}/300/450"


# Datos de práctica: los libros son reales, las calificaciones son inventadas
# y las sinopsis son resúmenes cortos escritos para este ejercicio.
BOOKS: list[Book] = [
    Book(id=1, title="Cien años de soledad", author="Gabriel García Márquez", year=1967,
         publisher="Editorial Sudamericana", genre="Realismo mágico",
         synopsis="La historia de la familia Buendía a lo largo de siete generaciones en el pueblo de Macondo.",
         rating=4.8, image_url=_cover("cien-anos")),
    Book(id=2, title="La ciudad y los perros", author="Mario Vargas Llosa", year=1963,
         publisher="Seix Barral", genre="Novela",
         synopsis="La vida de un grupo de cadetes en un colegio militar de Lima y la violencia que los rodea.",
         rating=4.5, image_url=_cover("ciudad-perros")),
    Book(id=3, title="El principito", author="Antoine de Saint-Exupéry", year=1943,
         publisher="Reynal & Hitchcock", genre="Fábula",
         synopsis="Un piloto perdido en el desierto conoce a un pequeño príncipe que viaja de planeta en planeta.",
         rating=4.7, image_url=_cover("principito")),
    Book(id=4, title="1984", author="George Orwell", year=1949,
         publisher="Secker & Warburg", genre="Distopía",
         synopsis="Winston Smith vive bajo un Estado que vigila y controla todo, hasta el pensamiento.",
         rating=4.6, image_url=_cover("mil-novecientos-ochenta-y-cuatro")),
    Book(id=5, title="Don Quijote de la Mancha", author="Miguel de Cervantes", year=1605,
         publisher="Francisco de Robles", genre="Novela",
         synopsis="Un hidalgo que leyó demasiados libros de caballería sale por el mundo a vivir aventuras.",
         rating=4.4, image_url=_cover("quijote")),
    Book(id=6, title="Rayuela", author="Julio Cortázar", year=1963,
         publisher="Editorial Sudamericana", genre="Novela experimental",
         synopsis="Una novela que se puede leer en más de un orden, entre París y Buenos Aires.",
         rating=4.3, image_url=_cover("rayuela")),
    Book(id=7, title="Los ríos profundos", author="José María Arguedas", year=1958,
         publisher="Editorial Losada", genre="Novela",
         synopsis="Ernesto, un niño que viaja por los Andes, descubre el mundo quechua y el internado donde estudia.",
         rating=4.5, image_url=_cover("rios-profundos")),
    Book(id=8, title="Fahrenheit 451", author="Ray Bradbury", year=1953,
         publisher="Ballantine Books", genre="Ciencia ficción",
         synopsis="En una sociedad donde los libros están prohibidos, un bombero empieza a dudar de su trabajo.",
         rating=4.2, image_url=_cover("fahrenheit")),
    Book(id=9, title="El Aleph", author="Jorge Luis Borges", year=1949,
         publisher="Editorial Losada", genre="Cuentos",
         synopsis="Colección de cuentos sobre el infinito, los laberintos y la memoria.",
         rating=4.6, image_url=_cover("aleph")),
    Book(id=10, title="Crónica de una muerte anunciada", author="Gabriel García Márquez", year=1981,
         publisher="La Oveja Negra", genre="Novela",
         synopsis="Todo el pueblo sabía que iban a matar a Santiago Nasar, y aun así nadie lo evitó.",
         rating=4.4, image_url=_cover("cronica-muerte")),
]
