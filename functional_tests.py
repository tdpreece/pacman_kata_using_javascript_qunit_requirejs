from selenium import webdriver

browser = webdriver.PhantomJS()
browser.get('file:///home/tdpreece/javascript_projects/pacman_javascript_qunit_requirejs/index.html')

assert 'PacMan' in browser.title
