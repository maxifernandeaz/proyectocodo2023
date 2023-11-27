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

// Function to remove an item from the cart
function removeItemFromCart(id) {
  shoppingCart = shoppingCart.filter(item => item.id !== id);
  // Update the cart display after removing the item
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

    // Create a span for the item details
    var detailsSpan = document.createElement('span');
    detailsSpan.textContent = `${item.name} x${item.quantity} - $${item.price * item.quantity}`;
    li.appendChild(detailsSpan);

    // Add a button to remove the item from the cart
    var removeButton = document.createElement('button');
    removeButton.textContent = 'Quitar';
    removeButton.onclick = function () {
      removeItemFromCart(item.id);
      // Update the cart display after removing the item
      updateCartDisplay();
    };

    li.appendChild(removeButton);
    cartList.appendChild(li);
  });

  // Update the total
  var cartTotal = document.getElementById('cart-total');
  var totalCost = calculateTotalCost();
  cartTotal.textContent = totalCost.toFixed(2);
}
