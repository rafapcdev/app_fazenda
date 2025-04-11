import io
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt

class MatplotlibImage(Image):
    def __init__(self, figure=None, **kwargs):
        super().__init__(**kwargs)
        self.figure = figure if figure else plt.Figure()
        self.update_figure()
    
    def update_figure(self, figure=None):
        if figure:
            self.figure = figure
        
        # Salva a figura em um buffer
        buf = io.BytesIO()
        canvas = FigureCanvasAgg(self.figure)
        canvas.draw()
        canvas.print_png(buf)
        buf.seek(0)
        
        # Carrega a imagem no widget Kivy
        img = CoreImage(buf, ext='png')
        self.texture = img.texture
        
        # Defina o tamanho da textura
        self.size = self.texture.size  # Ajusta o tamanho do widget para o tamanho da imagem

    def save_figure(self, filename):
        canvas = FigureCanvasAgg(self.figure)
        canvas.draw()
        canvas.print_figure(filename, dpi=100)
        return filename