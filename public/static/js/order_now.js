// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
	'use strict';

	// Fetch all the forms we want to apply custom Bootstrap validation styles to
	var forms = document.querySelectorAll('.needs-validation');

	// Loop over them and prevent submission
	Array.prototype.slice.call(forms).forEach(function (form) {
		form.addEventListener(
			'submit',
			function (event) {
				if (!form.checkValidity()) {
					event.preventDefault();
					event.stopPropagation();
				}

				form.classList.add('was-validated');
			},
			false
		);
	});
})();

// qty selector
qty_selector = document.getElementById('qty-selector');
qty_minus = document.getElementById('qty-minus');
qty_plus = document.getElementById('qty-plus');
qty_price = document.getElementById('qty-price-p');

qty_minus.addEventListener('click', function () {
	let current_qty = parseInt(qty_selector.value);
	let new_value = 0;
	if (current_qty <= 0) {
		new_value = 0;
		qty_selector.value = new_value;
	} else {
		new_value = parseInt(qty_selector.value) - 1;
		qty_selector.value = new_value;
	}

	qty_price.innerText = (new_value * 5.0).toFixed(2);
});

qty_plus.addEventListener('click', function () {
	let new_value = parseInt(qty_selector.value) + 1;
	qty_selector.value = new_value;
	qty_price.innerText = (new_value * 5.0).toFixed(2);
});
