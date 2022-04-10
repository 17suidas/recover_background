import os
import shutil
src = 'E:/大创/代码/爬取验证码代码/易盾/Necaptcha/'
dst = 'E:/大创/test/Necaptcha/'
if __name__ == '__main__':
    captcha_num = 0
    for captcha in os.listdir(src):
        print(src + captcha)
        shutil.copy(src + captcha, dst)
        captcha_num += 1
        if captcha_num == 2000:
            break

