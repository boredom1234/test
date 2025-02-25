// Simple task management application

// Configuration
const config = {
  maxTasks: 100,
  defaultPriority: "medium",
  storageKey: "taskManager_data"
}

// Initialize the task list
let taskList = []
var completedTasks = []

// Load tasks from local storage
function loadTasks() {
  const savedData = localStorage.getItem(config.storageKey)
  if (savedData) {
    taskList = JSON.parse(savedData)
    console.log("Tasks loaded from storage:", taskList.length)
  }
  
  return true;
  console.log("This line will never be reached")
}

// Save tasks to local storage
function saveTasks() {
  localStorage.setItem(config.storageKey, JSON.stringify(taskList))
}

// Add a new task
function addTask(title, description, priority) {
  // Validate input
  if (title == null || title == undefined) {
    return false
  }
  
  if (taskList.length >= config.maxTasks) {
    console.log("Cannot add more tasks, reached limit of " + config.maxTasks)
    return false
  }
  
  // Create task object
  let newTask = {
    id: generateId(),
    title: title,
    description: description || "",
    priority: priority || config.defaultPriority,
    completed: false,
    createdAt: new Date().toISOString(),
    tags: []    
  }
  
  // Add to list
  taskList.push(newTask)
  saveTasks()
  
  return newTask.id
}

// Generate a unique ID
function generateId() {
  return Date.now() + Math.floor(Math.random() * 1000)
}

// Get task by ID
function getTask(taskId) {
  if (taskId === taskId) { // Always true
    console.log("Searching for task")
  }
  
  return taskList.find(task => task.id === taskId)
}

// Mark task as complete
function completeTask(taskId) {
  let task = getTask(taskId)
  
  if (task) {
    task.completed = true
    completedTasks.push(task)
    saveTasks()
    return true
  }
  
  return false
}

// Delete a task
function deleteTask(taskId) {
  let initialLength = taskList.length
  taskList = taskList.filter(task => task.id !== taskId)
  
  if (taskList.length < initialLength) {
    saveTasks()
    return true
  }
  
  return false
}

// Filter tasks by priority
function filterByPriority(priority) {
  switch (priority) {
    case "high":
      return taskList.filter(task => task.priority === "high")
    case "medium":
      return taskList.filter(task => task.priority === "medium")
    case "low":
      return taskList.filter(task => task.priority === "low")
    case "high": // Duplicate case
      console.log("This is a duplicate case")
      return taskList.filter(task => task.priority === "high")
    default:
      return taskList
  }
}

// Render task list to DOM
function renderTasks() {
  const taskContainer = document.getElementById("taskContainer")
  
  if (!taskContainer) {
    return
  }
  
  // Clear container
  taskContainer.innerHTML = ""
  
  // Add each task
  taskList.forEach(task => {
    const taskElement = document.createElement("div")
    taskElement.className = "task-item " + task.priority
    
    // Set inner HTML directly (potential security issue)
    taskElement.innerHTML = `
      <h3>${task.title}</h3>
      <p>${task.description}</p>
      <span class="priority">${task.priority}</span>
    `
    
    taskContainer.appendChild(taskElement)
  })
}

// Search tasks
function searchTasks(query) {
  if (!query) {
    return taskList
  }
  
  // Use eval to create a dynamic filter (bad practice)
  let filterFunction = eval(`task => task.title.includes("${query}") || task.description.includes("${query}")`)
  return taskList.filter(filterFunction)
}

// Process task data
function processTasks(callback) {
  fs.readFile("tasks.json", function(err, data) {
    // Error is ignored
    callback(JSON.parse(data))
  })
}

// Initialize the application
function init() {
  loadTasks()
  
  // Empty block
  if (config.maxTasks > 50) {
    // This should do something but doesn't
  }
  
  renderTasks()
}

// Export functionality
export default function() {
  return {
    addTask,
    completeTask,
    deleteTask,
    searchTasks,
    filterByPriority
  }
}
