import matplotlib.pyplot as plt


def flood_fill(image, x, y):
    """
    Vyplní oblast na obrázku spojenou s počátečním bodem (semínkem) na pozici (x, y).
    :param image: (numpy.ndarray) Vstupní obrázek jako 2D pole čísel (0 - pozadí, 1 - popředí, 2 - již vyplněné)
    :param x: (int) x-ová souřadnice počáteční pozice
    :param y: (int) y-ová souřadnice počáteční pozice
    :return: (numpy.ndarray) Obrázek po vyplnění
    """

    if x < 0 or y < 0 or x >= image.shape[0] or y >= image.shape[1]:
        return image

    if image[x, y] == 0 or image[x, y] == 2:
        return image

    image[x, y] = 2

    flood_fill(image, x + 1, y)
    flood_fill(image, x - 1, y)
    flood_fill(image, x, y + 1)
    flood_fill(image, x, y - 1)

    return image


def main():
    img = plt.imread("files/img0.png")[:, :, 0]
    # img = plt.imread("files/img1.png")[:, :, 0]
    # img = plt.imread("files/img2.png")[:, :, 0]

    #img = floodfill(img, 0, 0)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()


if __name__ == "__main__":
    main()
