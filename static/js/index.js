const navList = document.querySelector('.nav-list'),
  navMenu = document.querySelector('.nav-menu'),
  navClose = document.querySelector('.nav-close'),
  navBg = document.querySelector('.nav-bg')


navMenu.addEventListener('click' , (e) => {
  navList.classList.toggle('!right-0')
  navBg.classList.toggle('hidden')
  document.body.classList.add('overflow-hidden')
})
navClose.addEventListener('click', () => {
  navList.classList.remove('!right-0')
  document.body.classList.remove('overflow-hidden')
  navBg.classList.toggle('hidden')
})
navBg.addEventListener('click' , () => {
  navList.classList.remove('!right-0')
  document.body.classList.remove('overflow-hidden')
  navBg.classList.toggle('hidden')
})

const year = document.querySelector(".year");
let today = new Date()
year.textContent = today.getFullYear()

const productBtn = document.querySelector('.product-btn')
const modalForm = document.querySelector('.modal-form')
const modalElement = document.querySelector('.modal-element')

productBtn.addEventListener('click' , () => {
  modalForm.classList.toggle('hidden')
  document.body.classList.toggle('overflow-hidden')
  setTimeout(() => {
    modalElement.classList.add('!scale-100', '!-translate-y-0')
  }, [5])
})
modalForm.addEventListener('click' , () => {
  modalForm.classList.toggle('hidden')
  document.body.classList.toggle('overflow-hidden')
  modalElement.classList.remove('!scale-100')
})

modalElement.addEventListener('click' , e => e.stopPropagation())

const isSucces = document.querySelector('.isSucces')
const successForm = document.querySelector('.success-form')
const successElement = document.querySelector('.success-element')