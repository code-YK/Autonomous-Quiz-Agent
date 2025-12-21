"use client"

import type React from "react"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Sparkles } from "lucide-react"

interface QuizInputProps {
  onGenerate: (text: string) => void
}

export function QuizInput({ onGenerate }: QuizInputProps) {
  const [text, setText] = useState("")

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (text.trim()) {
      onGenerate(text)
    }
  }

  return (
    <Card className="border-border">
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <Sparkles className="h-5 w-5 text-primary" />
          Generate Educational Quiz
        </CardTitle>
        <CardDescription>
          Paste educational text below to automatically generate a comprehensive quiz with concept extraction and
          difficulty ranking
        </CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit} className="space-y-4">
          <Textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Paste your educational text here... 

For example:
- Lecture transcripts
- Textbook chapters
- Study materials
- Course notes

The AI will analyze the content, extract key concepts, build a knowledge hierarchy, and generate questions with difficulty rankings."
            className="min-h-[300px] resize-none font-mono text-sm"
            required
          />
          <Button type="submit" size="lg" className="w-full sm:w-auto" disabled={!text.trim()}>
            <Sparkles className="mr-2 h-4 w-4" />
            Generate Quiz
          </Button>
        </form>
      </CardContent>
    </Card>
  )
}
