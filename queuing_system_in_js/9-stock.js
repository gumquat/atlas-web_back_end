const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const app = express();
const client = redis.createClient();

// Data
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

// Function to get item by id
function getItemById(id) {
  return listProducts.find(product => product.id === id);
}

// Route to list all products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Start the server
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Promisify Redis methods
const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

// Function to reserve stock by item ID
async function reserveStockById(itemId) {
  const reservedStock = await getAsync(`item.${itemId}`);
  if (reservedStock && parseInt(reservedStock) >= 1) {
    await setAsync(`item.${itemId}`, parseInt(reservedStock) - 1);
    return { status: 'Reservation confirmed', itemId: itemId };
  } else {
    return { status: 'Not enough stock available', itemId: itemId };
  }
}

// Route to reserve a product by item ID
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const product = listProducts.find(item => item.id === parseInt(itemId));
  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStatus = await reserveStockById(itemId);
  res.json(reservedStatus);
});

// Async function to get current reserved stock by item ID
async function getCurrentReservedStockById(itemId) {
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock ? parseInt(reservedStock) : 0;
}

// Route to get product details by item ID
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const product = listProducts.find(item => item.id === parseInt(itemId));
  if (!product) {
    return res.status(404).json({ error: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const availableStock = product.stock - reservedStock;

  res.json({
    id: product.id,
    name: product.name,
    price: product.price,
    stock: product.stock,
    reservedStock: reservedStock,
    availableStock: availableStock
  });
});

// Start the server
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});