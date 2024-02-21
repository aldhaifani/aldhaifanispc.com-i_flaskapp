const accordionItems = document.querySelectorAll('.collapse');
const acc = document.getElementById('accordionExample');

accordionItems.forEach((el) => {
	el.addEventListener('shown.bs.collapse', (e) => {
		var scrollOffset = acc.scrollTop + el.parentNode.offsetTop - 70;
		window.scroll({
			top: scrollOffset,
			left: 0,
			behavior: 'smooth',
		});
	});
});
