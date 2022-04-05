import pytest

case_01_valid = pytest.param(
    "case_01.txt",
    [
        ["Panqueca de carne moída", 100, 52, 2, 5],
        ["Ovo", 100, 52, 2, 5],
        ["Kibe de forno", 100, 52, 2, 5],
        ["Hambúrguer caseiro", 100, 52, 2, 5],
        ["salmão", 100, 52, 2, 5],
        ["Whey Protein", 100, 51, 2, 5]
    ],
    id="case_01_valid",
)
case_02_valid = pytest.param(
    "case_02.txt",
    [
        ["Língua bovina", 100, 52, 2, 5],
        ["Dobradinha", 100, 52, 2, 5],
        ["Coração", 100, 52, 2, 5],
        ["Pernil", 100, 52, 2, 5]
    ],
    id="case_02_valid",
)
case_03_valid = pytest.param(
    "case_03.txt",
    [
        ["Macarrão cozido", 100, 5, 22, 5],
        ["Nhoque sem molho", 100, 5, 22, 5],
        ["Batata inglesa cozida", 100, 5, 22, 5],
        ["Cará, Inhame ou mandioquinha", 100, 5, 22, 5],
        ["Aipim", 100, 50, 22, 5],
        ["Atum enlatado", 100, 51, 2, 5],
        ["Sardinha enlatada", 100, 51, 2, 5],
        ["Bacalhau", 100, 51, 2, 5],
        ["Polvo", 100, 52, 2, 5]
    ],
    id="case_03_valid",
)
case_04_valid = pytest.param(
    "case_04.txt",
    [
        ["Pão italiano", 100, 5, 22, 5],
        ["Bisnaguinha", 100, 5, 22, 5],
        ["Torrada integral", 100, 5, 22, 5],
        ["Bolacha água e sal", 100, 5, 22, 5],
        ["Biscoito doce sem recheio", 100, 5, 22, 5],
        ["Nesfit", 100, 5, 22, 5],
        ["Bolacha de arroz integral", 100, 5, 22, 5],
        ["Aveia", 100, 5, 22, 5],
        ["Sardinha fresca", 100, 53, 2, 5],
        ["Arroz integral", 100, 5, 22, 5]
    ],
    id="case_04_valid",
)
case_05_valid = pytest.param(
    "case_05.txt",
    [
        ["Carne moída", 100, 51, 2, 5],
        ["Carne assada", 100, 53, 2, 5],
        ["Bife de fígado", 100, 51, 2, 5],
        ["Proteína de soja", 100, 52, 2, 5],
        ["Tofu", 100, 51, 2, 5],
        ["Coxa ou sobre-coxa de frango", 100, 53, 2, 5],
        ["Carne de porco magra grelhada", 100, 51, 2, 5],
        ["Carne seca", 100, 52, 2, 5],
        ["Camarão cozido", 100, 51, 22, 5],
        ["Peixe assado", 100, 51, 2, 5],
        ["Pão Árabe integral", 100, 5, 22, 5],
        ["Pão francês (integral)", 100, 5, 22, 5]
    ],
    id="case_05_valid",
)
case_06_valid = pytest.param(
    "case_06.txt",
    [
        ["Cream cheese light", 100, 5, 22, 32],
        ["Pasta de soja", 100, 5, 22, 50],
        ["Requeijão light 1 colher de sopa", 100, 5, 22, 51],
        ["Creme de ricota", 100, 5, 22, 51],
        ["chester", 100, 5, 22, 51],
        ["peru", 100, 11, 2, 5],
        ["Pasta de amendoim integral", 100, 3, 2, 53],
        ["Óleo", 100, 4, 2, 53],
        ["Azeite", 100, 4, 2, 54],
        ["Oleo de coco", 100, 3, 2, 54],
        ["Bife grelhado", 100, 52, 22, 5],
        ["filé de frango grelhado", 100, 51, 2, 5],
        ["Frango assado", 100, 51, 2, 5],
        ["Almôndegas", 100, 52, 2, 5],
        ["Bife rolé", 100, 53, 22, 5],
        ["Picadinho", 100, 53, 2, 5],
        ["Carne ensopada", 100, 51, 2, 5]
    ],
    id="case_06_valid",
)
case_07_valid = pytest.param(
    "case_07.txt",
    [
        ["iogurte desnatado", 100, 5, 22, 52],
        ["Leite em pó desnatado", 100, 5, 22, 53],
        ["Leite de soja", 100, 5, 22, 51],
        ["Leite", 100, 5, 22, 51],
        ["iogurte integral", 100, 5, 22, 51],
        ["Leite em pó integral", 100, 5, 22, 51],
        ["Coalhada", 100, 5, 22, 51],
        ["Queijo minas frescal", 100, 5, 22, 51],
        ["Ricota", 100, 5, 22, 52],
        ["Queijo minas curado", 100, 5, 22, 50],
        ["Requeijão", 100, 5, 22, 34],
        ["Requeijão light", 100, 5, 22, 34],
        ["Queijo cottage", 100, 5, 22, 32],
        ["Cream cheese", 100, 5, 22, 51],
    ],
    id="case_07_valid",
)
case_08_valid = pytest.param(
    "case_08.txt",
    [
        ["Tabule", 100, 5, 22, 5],
        ["Pão de forma integral", 100, 5, 22, 5],
        ["Pão de hambúrguer integral 1 unidade", 100, 5, 22, 5],
        ["granola", 100, 5, 22, 5],
        ["linhaça", 100, 5, 22, 5],
        ["chia", 100, 5, 22, 5],
        ["Bolo simples", 100, 5, 22, 5],
        ["Barra de cereais", 100, 5, 22, 5],
        ["Tapioca", 100, 5, 22, 5],
        ["Pipoca salgada", 100, 5, 22, 5],
        ["Leite", 100, 5, 22, 51],
    ],
    id="case_08_valid",
)
case_09_valid = pytest.param(
    "case_09.txt",
    [
        ["Queijo prato", 100, 5, 22, 12],
        ["Queijo provolone", 100, 5, 22, 30],
        ["Queijo parmesão", 100, 5, 22, 51],
        ["Queijo tipo polenguinho", 100, 5, 22, 51],
        ["Margarina", 100, 5, 22, 51],
        ["manteiga", 100, 5, 22, 51],
        ["Requeijão", 100, 5, 22, 51],
        ["Arroz branco", 100, 5, 30, 2],
        ["Purê de batata", 100, 5, 22, 5],
        ["Farofa simples", 100, 5, 22, 5],
        ["Batata doce", 100, 5, 22, 5],
        ["Milho cozido", 100, 5, 22, 5],
        ["Milho em conserva", 100, 5, 22, 5],
        ["Quinua", 100, 5, 22, 5],
        ["Amaranto", 100, 5, 22, 5],
        ["Trigo", 100, 5, 22, 5],
    ],
    id="case_09_valid",
)
case_10_duplicate_name = pytest.param(
    "case_10_duplicate_name.txt",
    [
        ["Pasta de soja", 100, 5, 22, 50],
        ["Pasta de soja", 100, 2, 2, 51],
    ],
    id="case_10_duplicate_name",
)