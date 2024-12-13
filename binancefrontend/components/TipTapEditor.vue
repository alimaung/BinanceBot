<script setup>
import { useEditor, EditorContent } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'

const props = defineProps({
  modelValue: {
    type: String,
    default: ''
  },
})

const emit = defineEmits(['update:modelValue'])

const editor = useEditor({
  content: props.modelValue,
  extensions: [
    StarterKit,
  ],
  onUpdate: ({ editor }) => {
    emit('update:modelValue', editor.getHTML())
  }
})

// Cleanup editor on component unmount
onBeforeUnmount(() => {
  if (editor.value) {
    editor.value.destroy()
  }
})

// Toolbar button configuration
const toolbarButtons = [
  // Text Formatting
  { 
    action: 'toggleBold', 
    icon: 'format_bold', 
    isActive: (editor) => editor.isActive('bold'),
    canExecute: (editor) => editor.can().toggleBold()
  },
  { 
    action: 'toggleItalic', 
    icon: 'format_italic', 
    isActive: (editor) => editor.isActive('italic'),
    canExecute: (editor) => editor.can().toggleItalic()
  },
  { 
    action: 'toggleStrike', 
    icon: 'strikethrough_s', 
    isActive: (editor) => editor.isActive('strike'),
    canExecute: (editor) => editor.can().toggleStrike()
  },
  { 
    action: 'toggleCode', 
    icon: 'code', 
    isActive: (editor) => editor.isActive('code'),
    canExecute: (editor) => editor.can().toggleCode()
  },
]

// Heading Buttons with Corrected Icons
const headingButtons = [1, 2, 3, 4, 5, 6].map(level => ({
  action: `toggleHeading_${level}`,
  icon: level <= 2 ? `looks_${level === 1 ? 'one' : 'two'}` : `looks_${level}`,
  isActive: (editor) => editor.isActive('heading', { level }),
  execute: (editor) => editor.chain().focus().toggleHeading({ level }).run()
}))

// List and Block Formatting
const blockButtons = [
  { 
    action: 'toggleBulletList', 
    icon: 'format_list_bulleted', 
    isActive: (editor) => editor.isActive('bulletList'),
  },
  { 
    action: 'toggleOrderedList', 
    icon: 'format_list_numbered', 
    isActive: (editor) => editor.isActive('orderedList'),
  },
  { 
    action: 'toggleCodeBlock', 
    icon: 'code_blocks', 
    isActive: (editor) => editor.isActive('codeBlock'),
  },
  { 
    action: 'toggleBlockquote', 
    icon: 'format_quote', 
    isActive: (editor) => editor.isActive('blockquote'),
  },
  { 
    action: 'setParagraph', 
    icon: 'segment', 
    isActive: (editor) => editor.isActive('paragraph'),
  },
]

// Additional Utility Buttons
const utilityButtons = [
  { 
    action: 'unsetAllMarks', 
    icon: 'format_clear',
    execute: (editor) => editor.chain().focus().unsetAllMarks().run()
  },
  { 
    action: 'clearNodes', 
    icon: 'delete',
    execute: (editor) => editor.chain().focus().clearNodes().run()
  },
  { 
    action: 'setHorizontalRule', 
    icon: 'horizontal_rule',
    execute: (editor) => editor.chain().focus().setHorizontalRule().run()
  },
  { 
    action: 'setHardBreak', 
    icon: 'keyboard_return',
    execute: (editor) => editor.chain().focus().setHardBreak().run()
  },
]

// History Buttons
const historyButtons = [
  { 
    action: 'undo', 
    icon: 'undo',
    canExecute: (editor) => editor.can().undo(),
  },
  { 
    action: 'redo', 
    icon: 'redo',
    canExecute: (editor) => editor.can().redo(),
  },
]

// Utility function to execute editor commands
const executeEditorCommand = (button) => {
  if (!editor.value) return

  if (button.execute) {
    // For buttons with custom execute method
    button.execute(editor.value)
  } else {
    // For standard chain commands
    const command = button.action.includes('_') 
      ? button.action.split('_')[1] 
      : button.action

    editor.value.chain().focus()[command]().run()
  }
}
</script>

<template>
    <div class="tiptap-editor">
        <div v-if="editor" class="editor-toolbar">
            <div class="toolbar-section">
                <button 
                    v-for="button in toolbarButtons" 
                    :key="button.action"
                    @click="executeEditorCommand(button)"
                    :disabled="button.canExecute && !button.canExecute(editor)"
                    :class="{ 'is-active': button.isActive(editor) }"
                    tooltip="tooltip"
                >
                <span class="material-symbols-outlined">{{ button.icon }}</span>
                </button>

                <button 
                    v-for="button in headingButtons" 
                    :key="button.action"
                    @click="executeEditorCommand(button)"
                    :class="{ 'is-active': button.isActive(editor) }"
                >
                <span class="material-symbols-outlined">{{ button.icon }}</span>
                </button>

                <button 
                    v-for="button in blockButtons" 
                    :key="button.action"
                    @click="executeEditorCommand(button)"
                    :class="{ 'is-active': button.isActive(editor) }"
                >
                <span class="material-symbols-outlined">{{ button.icon }}</span>
                </button>

                <button 
                    v-for="button in utilityButtons" 
                    :key="button.action"
                    @click="executeEditorCommand(button)"
                >
                <span class="material-symbols-outlined">{{ button.icon }}</span>
                </button>

                <button 
                    v-for="button in historyButtons" 
                    :key="button.action"
                    @click="executeEditorCommand(button)"
                    :disabled="button.canExecute && !button.canExecute(editor)"
                >
                <span class="material-symbols-outlined">{{ button.icon }}</span>
                </button>
            </div>
        </div>
        
        <EditorContent 
        :editor="editor" 
        class="tiptap-editor-content"
        
        />
    </div>
</template>

<style scoped>
.tiptap-editor {
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  
}

.editor-toolbar {
  display: flex;
  flex-direction: row;
  gap: 0.5rem;
  padding: 0.5rem;
  border-bottom: 1px solid #e0e0e0;
}

.toolbar-section {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  margin-right: 1rem;
}

.toolbar-section h4 {
  margin: 0 0 0.5rem 0;
  font-size: 0.75rem;
}

.toolbar-section {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.toolbar-section button {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.25rem;
  border-radius: 4px;
  margin: 2px;
  
}

.toolbar-section button:hover {
  border: 1px solid #e0e0e0;
}

.toolbar-section button.is-active {
  
}

.toolbar-section button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.tiptap-editor-content {
  margin: 20px;
  margin-left: 30px;
}
</style>