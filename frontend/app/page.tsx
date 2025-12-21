"use client"
const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL

import { useState } from "react"
import { QuizInput } from "@/components/quiz-input"
import { ProcessingSteps } from "@/components/processing-steps"
import { QuizResults } from "@/components/quiz-results"
import type { QuizResponse } from "@/lib/types"

export default function Home() {
  const [isProcessing, setIsProcessing] = useState(false)
  const [results, setResults] = useState<QuizResponse | null>(null)
  const [currentStep, setCurrentStep] = useState(0)

  const handleGenerate = async (text: string) => {
    setIsProcessing(true)
    setResults(null)
    setCurrentStep(0)

    const steps = ["Extracting concepts", "Building hierarchy", "Generating quiz", "Ranking difficulty", "Validation"]

    // Simulate step progression
    const stepInterval = setInterval(() => {
      setCurrentStep((prev) => {
        if (prev < steps.length - 1) return prev + 1
        clearInterval(stepInterval)
        return prev
      })
    }, 800)

    try {
      const response = await fetch(`${API_BASE_URL}/quiz/generate`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
      })

      if (!response.ok) {
        throw new Error("Failed to generate quiz")
      }

      const data: QuizResponse = await response.json()
      clearInterval(stepInterval)
      setResults(data)
    } catch (error) {
      console.error("[v0] Error generating quiz:", error)
      clearInterval(stepInterval)
      alert("Failed to generate quiz. Please ensure the backend is running.")
    } finally {
      setIsProcessing(false)
    }
  }

  const handleReset = () => {
    setResults(null)
    setCurrentStep(0)
  }

  return (
    <div className="min-h-screen bg-background">
      <header className="border-b border-border bg-card">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-4 sm:py-6">
          <h1 className="text-2xl sm:text-3xl font-bold tracking-tight text-foreground">Autonomous Quiz Agent</h1>
          <p className="mt-1 text-sm text-muted-foreground">AI-powered educational quiz generation system</p>
        </div>
      </header>

      <main className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8 sm:py-12">
        {!results && !isProcessing && <QuizInput onGenerate={handleGenerate} />}

        {isProcessing && <ProcessingSteps currentStep={currentStep} />}

        {results && <QuizResults results={results} onReset={handleReset} />}
      </main>
    </div>
  )
}
