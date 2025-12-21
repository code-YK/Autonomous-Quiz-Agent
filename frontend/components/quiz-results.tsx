"use client"

import { Button } from "@/components/ui/button"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { ConceptsSection } from "@/components/sections/concepts-section"
import { HierarchySection } from "@/components/sections/hierarchy-section"
import { QuestionsSection } from "@/components/sections/questions-section"
import { ValidationSection } from "@/components/sections/validation-section"
import { AgentGraphSection } from "@/components/sections/agent-graph-section"
import type { QuizResponse } from "@/lib/types"
import { RotateCcw } from "lucide-react"

interface QuizResultsProps {
  results: QuizResponse
  onReset: () => void
}

export function QuizResults({ results, onReset }: QuizResultsProps) {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-foreground">Quiz Generated Successfully</h2>
          <p className="text-sm text-muted-foreground mt-1">Explore the results across different sections below</p>
        </div>
        <Button onClick={onReset} variant="outline" size="sm">
          <RotateCcw className="mr-2 h-4 w-4" />
          Generate New Quiz
        </Button>
      </div>

      <Tabs defaultValue="questions" className="w-full">
        <TabsList className="grid w-full grid-cols-2 sm:grid-cols-5 gap-1">
          <TabsTrigger value="questions">Questions</TabsTrigger>
          <TabsTrigger value="concepts">Concepts</TabsTrigger>
          <TabsTrigger value="hierarchy">Hierarchy</TabsTrigger>
          <TabsTrigger value="validation">Validation</TabsTrigger>
          <TabsTrigger value="graph">Agent Graph</TabsTrigger>
        </TabsList>

        <TabsContent value="questions" className="mt-6">
          <QuestionsSection questions={results.ranked_questions} />
        </TabsContent>

        <TabsContent value="concepts" className="mt-6">
          <ConceptsSection concepts={results.concepts} />
        </TabsContent>

        <TabsContent value="hierarchy" className="mt-6">
          <HierarchySection hierarchy={results.hierarchy} />
        </TabsContent>

        <TabsContent value="validation" className="mt-6">
          <ValidationSection
            validationPassed={results.validation_passed}
            validationFeedback={results.validation_feedback}
            retryCount={results.retry_count}
          />
        </TabsContent>

        <TabsContent value="graph" className="mt-6">
          <AgentGraphSection />
        </TabsContent>
      </Tabs>
    </div>
  )
}
