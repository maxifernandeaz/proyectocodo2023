// Define a global variable for the shopping cart
var shoppingCart = [];

// Function to add items to the cart
function addToCart(id, name, quantity) {
  // Check if the item is already in the cart
  var existingItem = shoppingCart.find(item => item.id === id);

  if (existingItem) {
    // If the item exists, update the quantity
    existingItem.quantity += quantity;
  } else {
    // If the item is not in the cart, add it
    shoppingCart.push({ id, name, quantity, price: Number(document.querySelector('.add-to-cart-btn').getAttribute('data-price')) });
  }

  // Update the cart display
  updateCartDisplay();
}

// Function to calculate the total cost
function calculateTotalCost() {
  return shoppingCart.reduce((acc, item) => {
    return acc + (item.price * item.quantity);
  }, 0);
}

// Function to update the cart display
function updateCartDisplay() {
  // Update the cart list
  var cartList = document.getElementById('cart-list');
  cartList.innerHTML = '';

  shoppingCart.forEach(item => {
    var li = document.createElement('li');
    li.textContent = `${item.name} x${item.quantity} - $${item.price * item.quantity}`;
    cartList.appendChild(li);
  });

  // Update the total
  var cartTotal = document.getElementById('cart-total');
  var totalCost = calculateTotalCost();
  cartTotal.textContent = totalCost.toFixed(2);
}
function redirectToPayment() {
  // Redirect to "Pago.html"
  window.location.href = 'Pago.html';
}