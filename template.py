from pygame import *
from settings import *

# 設定
init()
screen = display.set_mode((WIDTH, HEIGHT))
clock  = time.Clock()

# 定義(クラス・関数)

# 準備(スプライト・マップ・変数)
all_sprites = sprite.Group()
{SPRITE_GROUPS}

# メインループ
run = True
while run:
    # イベント
    for e in event.get():
        if e.type == QUIT:
            run = False
        {EVENT_ACTIONS}

    # 更新
    alls.update()

    # 判定
    {COLLISIONS} 
    {GAME_ACTIONS}  

    # 描画
    screen.fill({BG})
    alls.draw(screen)
    {UI_DRAW}  
    display.flip()

    clock.tick(FPS)

quit()
